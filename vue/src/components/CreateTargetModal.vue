<template>
    <div>
        <b-button class="float-left" v-b-modal.candidate-from-target-modal variant="outline-primary" :disabled="alerts.length === 0">Add Candidates from Alerts</b-button>
        <b-modal id="candidate-from-target-modal" size="xl" title="Create Candidate(s) from Alerts">
            <!-- TODO: display targets to be created -->
            <b-container>
                <b-form @submit="onCandidateFromAlert">
                    <b-form-row>
                        <b-form-checkbox-group>
                            <b-form-checkbox v-for="group in userGroups" :key="group.name" :value="group.id" @change="onSelectGroup">
                                {{ group.name }}
                            </b-form-checkbox>
                        </b-form-checkbox-group>
                    </b-form-row>
                </b-form>
            </b-container>
            <template #modal-footer="{ cancel }">
                <b-button class="float-right" @click="onCandidateFromAlert" variant="primary">Add Candidates</b-button>
                <b-button class="float-right" @click="cancel()">Cancel</b-button>
            </template>
        </b-modal>
    </div>
</template>

<script>
    import _ from 'lodash';
    import axios from 'axios';

    export default {
        components: {
        },
        props: {
            alerts: {
                type: Array,
                required: false
            },
            supereventId: {
                type: Number,
                required: true
            }
        },
        data() {
            return {
                selectedGroups: [],
                userGroups: []
            }
        },
        mounted() {
            this.$root.$on('bv::modal::show', (bvEvent, modalId) => {
                axios  // get groups available to user
                    .get(`${this.$store.state.tomApiBaseUrl}/api/groups/`, this.$store.state.tomAxiosConfig)
                    .then(response => {
                        this.userGroups = response['data']['results'];
                    })
                    .catch(error => {
                        console.log(`Unable to retrieve groups: ${error}.`)
                    });
                });
        },
        methods: {
            onCandidateFromAlert() {
                let createdTargetPromises = [];
                this.alerts.forEach(alert => {
                    let target_data = {
                        name: alert['identifier'],
                        ra: alert['right_ascension'],
                        dec: alert['declination'],
                        type: 'SIDEREAL',
                        aliases: [],
                        targetextra_set: [],
                        groups: this.selectedGroups.map(group => ({id: group}))
                    };
                    createdTargetPromises.push(
                        axios.post(`${this.$store.state.tomApiBaseUrl}/api/targets/`, target_data, this.$store.state.tomAxiosConfig)
                    );
                });

                Promise
                    .all(createdTargetPromises) // Wait for all targets to be created
                    .then(response => {
                        // create event candidates from new targets
                        let eventCandidateData = response.map(targetResponse => (
                            {superevent: this.supereventId, target: targetResponse.data.id}
                        ));
                        axios
                            .post(`${this.$store.state.tomApiBaseUrl}/api/eventcandidates/`, eventCandidateData)
                            .then(response => {
                                this.$bvModal.hide('candidate-from-target-modal');
                                this.$emit('created-target-candidates', response.data.length);
                            })
                            .catch(error => {
                                console.log(`Unable to create eventcandidates for new targets: ${error}`);
                            });
                    })
                    .catch(error => {
                        console.log(`Unable to create event candidates: ${error}`)
                    });
            },
            onSelectGroup(row, event) {
                if (event === true) {
                    // add group to list
                    if (!_.includes(this.selectedGroups, row.item)) this.selectedGroups.push(row.item);
                } else {
                    // remove target from list
                    this.selectedGroups = this.selectedGroups.filter(function(value){
                        return value !== row.item;
                    });
                }
            }
        }
    }
</script>