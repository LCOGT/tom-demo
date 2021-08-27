<template>
    <div>
        <b-button class="float-right mx-1" @click="onCreateFromAlerts" variant="outline-primary">Add Candidates from Alerts</b-button>
        <b-button class="float-right" v-b-modal.candidate-form-modal variant="outline-primary">Add Candidate from Existing Target</b-button>
        <b-modal id="candidate-form-modal" size="xl" title="Add Event Candidate">
            <b-container>
                <b-form @submit="onCreateCandidates">
                    <b-form-input id="target-name-input" v-model="form.name" placeholder="Target Name" @input="targetSearch" required />
                    <b-form-input id="target-ra-input" v-model="form.ra" placeholder="Right Ascension" @input="targetSearch" required />
                    <b-form-input id="target-dec-input" v-model="form.dec" placeholder="Declination" @input="targetSearch" required />
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
                selectedAlerts: [],
                selectedTargets: [],
            }
        },
        mounted() {
            console.log('mounted add candidate modal');
            axios
                .get(`${this.$store.state.tomApiBaseUrl}/api/targets/`)
                .then(response => {
                    this.matches = response['data']['results'];
                    console.log(`re-mounted: ${this.matches}`);
                })
                .catch(error => {
                        console.log(`Unable to retrieve targets: ${error}.`);
                    }
                )
        },
        methods: {
            targetSearch() {
                console.log('targetSearch');
                // TODO: filter out targets that are already associated with this superevent
                let params = `name=${this.form.name}`;
                if (this.form.ra !== '' && this.form.dec !== '') {  // TODO: make this check more robust
                    params += `&cone_search=${this.form.ra},${this.form.dec},5`;
                }
                axios
                    .get(`${this.$store.state.tomApiBaseUrl}/api/targets/?${params}`)
                    .then(response => {
                        this.matches = response['data']['results'];
                    })
                    .catch(error => {
                        console.log(`Unable to retrieve any matching targets: ${error}.`);
                    })
            },
            onCreateCandidates() {  // TODO: require >1 candidate to select
                let event_candidate_data = []
                this.selectedTargets.forEach(target => event_candidate_data.push(
                    {superevent: this.supereventId, target: target}
                ));
                axios
                    .post(`${this.$store.state.tomApiBaseUrl}/api/eventcandidates/`, event_candidate_data)
                    .then(response => {
                        console.log(`Successfully created event candidates: ${response}`)
                        this.$bvModal.hide('candidate-form-modal');
                        this.$emit('created-candidates', response.data.length);
                    })
                    .catch(error => {
                        console.log(`Unable to create event candidates: ${error}`)
                    })
                this.selectedTargets = [];
            },
            onCreateFromAlerts() {
                // let alert_candidate_data = []
                // this.selectedAlerts.forEach(alert => {
                //     let target_data = {

                //     };
                //     axios
                //         .post(`${this.tomApiBaseUrl}/api/targets/`, )
                // });
            },
            onSelectAlert(row, event) {
                this.onSelectItem(row.item, event, this.selectedAlerts)
            },
            onSelectItem(item, event, list) {
                if (event === true) {
                    // add target to list
                    if (!_.includes(list, item)) list.push(item);
                } else {
                    // remove target from list
                    list = list.filter(function(value){
                        return value != item;
                    });
                }
            },
            onSelectTarget(row, event) {
                this.onSelectItem(row.item.id, event, this.selectedTargets);
            }
        }
    }
</script>
