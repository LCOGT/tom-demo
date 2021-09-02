<template>
    <div>
        <b-button class="float-left" v-b-modal.candidate-form-modal variant="outline-primary">Add Candidate from Existing Target</b-button>
        <b-modal id="candidate-form-modal" size="xl" title="Add Event Candidate">
            <b-container>
                <b-form @submit="onCreateCandidates">
                    <b-form-row>
                        <b-col>
                            <b-form-input id="target-name-input" v-model="form.name" placeholder="Target Name" @input="targetSearch" required />
                        </b-col>
                        <b-col>
                            <b-form-input id="target-ra-input" v-model="form.ra" placeholder="Right Ascension" @input="targetSearch" required />
                        </b-col>
                        <b-col>
                            <b-form-input id="target-dec-input" v-model="form.dec" placeholder="Declination" @input="targetSearch" required />
                        </b-col>
                    </b-form-row>
                </b-form>
                <hr />
                <selectable-target-table :targets="matches" @selected-target="onSelectTarget" />
            </b-container>
            <template #modal-footer="{ cancel }">
                <b-button class="float-right" @click="onCreateCandidates" variant="primary">Add Candidates</b-button>
                <b-button class="float-right" @click="cancel()">Cancel</b-button>
            </template>
        </b-modal>
    </div>
</template>

<script>
    import _ from 'lodash';
    import axios from 'axios';
    import SelectableTargetTable from '@/components/SelectableTargetTable.vue';

    export default {
        components: {
            SelectableTargetTable
        },
        props: {
            supereventId: {
                type: Number,
                required: true
            },
            existingEventCandidates: {
                type: Array,
                required: false
            },
        },
        data() {
            return {
                form: {
                    name: '',
                    ra: '',
                    dec: ''
                },
                matches: [],
                selectedTargets: [],
                userGroups: []
            }
        },
        mounted() {
            axios  // Get all public targets in TOM
                .get(`${this.$store.state.tomApiBaseUrl}/api/targets/`, this.$store.state.tomAxiosConfig)
                .then(response => {
                    // Filter out targets that are already associated with the superevent--this should be broken into a reusable method
                    this.matches = response['data']['results'];
                    this.matches = this.matches.filter(value => {
                        let match = false;
                        this.existingEventCandidates.forEach(eventCandidate => {
                            if (value.id === eventCandidate.id) match = true;
                        });
                        return !match;
                    })
                })
                .catch(error => {
                        console.log(`Unable to retrieve targets: ${error}.`);
                    }
                )
            /* WIP - get user groups and add them to target form
                axios
                    .get(`${this.$store.state.tomApiBaseUrl}/api/groups/`, this.$store.state.tomAxiosConfig)
                    .then(response => {
                        console.log('user groups');
                        this.userGroups = response['data']['results']
                        console.log(this.userGroups);
                    })
                    .catch(error => {
                        console.log(`Unable to retrieve user groups: ${error}.`);
                    })
            */
        },
        methods: {
            targetSearch() {  // Search for targets using form data in modal
                let params = `name=${this.form.name}`;
                if (this.form.ra !== '' && this.form.dec !== '') {  // TODO: make this check more robust for negative declination
                    params += `&cone_search=${this.form.ra},${this.form.dec},5`;
                }
                axios
                    .get(`${this.$store.state.tomApiBaseUrl}/api/targets/?${params}`, this.$store.state.tomAxiosConfig)
                    .then(response => {
                        // Filter out targets that are already associated with the superevent--this should be broken into a reusable method
                        this.matches = response['data']['results'];
                        this.matches = this.matches.filter(value => {
                            let match = false;
                            this.existingEventCandidates.forEach(eventCandidate => {
                                if (value.id === eventCandidate.id) match = true;
                            });
                            return !match;
                        })
                    })
                    .catch(error => {
                        console.log(`Unable to retrieve any matching targets: ${error}.`);
                    })
            },
            createEventCandidates(eventCandidateData, callback) {  // Create event candidates and call callback function with number of created eventCandidates
                axios
                    .post(`${this.$store.state.tomApiBaseUrl}/api/eventcandidates/`, eventCandidateData)
                    .then(response => {
                        let numCandidates;
                        if (Array.isArray(response.data)) {  // If multiple event candidates were created, API endpoint returns a list
                            numCandidates = response.data.length;
                        } else {
                            numCandidates = 1;
                        }
                        callback(numCandidates);
                    })
                    .catch(error => {
                        console.log(`Unable to create event candidates: ${error}`)
                    })
            },
            onCreateCandidates() {  // TODO: require >1 candidate to select, possibly split into multiple events, also add form validation
                if (this.selectedTargets.length !== 0) {  // Check if any targets are selected
                    let eventCandidateData = []
                    this.selectedTargets.forEach(target => eventCandidateData.push(  // Populate form data with event candidate data
                        {superevent: this.supereventId, target: target}
                    ));
                    this.createEventCandidates(eventCandidateData, (numCandidates) => {
                        this.$bvModal.hide('candidate-form-modal');
                        this.$emit('created-candidates', numCandidates);
                    });
                } else if (this.form.name !== '' && this.form.ra !== '' && this.form.dec !== '') {  // If target data is present and no event candidates are selected
                    let targetData = {
                        name: this.form.name, ra: this.form.ra, dec: this.form.dec, type: 'SIDEREAL', aliases: [],
                        targetextra_set: []
                    };
                    axios
                        .post(`${this.$store.state.tomApiBaseUrl}/api/targets/`, targetData)
                        .then(response => {
                            let targetId = response.data.id;
                            this.createEventCandidates({superevent: this.supereventId, target: targetId}, (numCandidates) => {
                                this.$bvModal.hide('candidate-form-modal');
                                this.$emit('created-candidates', numCandidates);
                            })
                        })
                        .catch(error => {  // TODO: display error in modal
                            console.log(`Unable to create target: ${error}`);
                        });
                    this.form = {name: '', ra: '', dec: ''};
                }
                this.selectedTargets = [];
            },
            onSelectTarget(row, event) {  // TODO: move to a utils.js
                if (event === true) {
                // add target to list
                if (!_.includes(this.selectedTargets, row.item.id)) this.selectedTargets.push(row.item.id);
            } else {
                // remove target from list
                this.selectedTargets = this.selectedTargets.filter(function(value) {
                    return value !== row.item.id;
                });
            }
            }
        }
    }
</script>
