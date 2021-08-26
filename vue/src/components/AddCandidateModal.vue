<template>
    <div>
        <b-button v-b-modal.candidate-form-modal>Add Candidate</b-button>
        <b-modal id="candidate-form-modal" size="xl" title="Add Event Candidate">
            <b-form @submit="onCreateCandidate">
                <b-form-input id="target-name-input" v-model="form.name" placeholder="Target Name" @input="targetSearch" required />
                <b-form-input id="target-ra-input" v-model="form.ra" placeholder="Right Ascension" @input="targetSearch" required />
                <b-form-input id="target-dec-input" v-model="form.dec" placeholder="Declination" @input="targetSearch" required />
            </b-form>
            <hr />
            <selectable-target-table :targets="matches" @selected-target="onSelectTarget" />
            <template #modal-footer>
                <div>
                    <b-button class="float-right" @click="onCreateCandidates" variant="primary">Add Candidates</b-button>
                    <b-button class="float-right" @click="show = false">Cancel</b-button>
                </div>
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
            }
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
            }
        },
        mounted() {
            console.log('mounted add candidate modal');
            axios
                .get('http://localhost:8000/api/targets/')
                .then(response => {
                    this.matches = response['data']['results'];
                })
                .catch(error => {
                        console.log(`Unable to retrieve targets: ${error}.`);
                    }
                )
        },
        methods: {
            targetSearch() {
                // TODO: filter out targets that are already associated with this superevent
                let params = `name=${this.form.name}`;
                if (this.form.ra !== '' && this.form.dec !== '') {  // TODO: make this check more robust
                    params += `&cone_search=${this.form.ra},${this.form.dec},5`;
                }
                axios
                    .get(`http://localhost:8000/api/targets/?${params}`)
                    .then(response => {
                        console.log(response);
                        this.matches = response['data']['results'];
                        console.log(this.matches);
                    })
                    .catch(error => {
                        console.log(`Unable to retrieve any matching targets: ${error}.`);
                    })
            },
            onCreateCandidates() {
                let event_candidate_data = []
                this.selectedTargets.forEach(target => event_candidate_data.push(
                    {superevent: this.supereventId, target: target}
                ));
                axios
                    .post(`http://localhost:8000/api/eventcandidates/`, event_candidate_data)
                    .then(response => {
                        console.log(`Successfully created event candidates: ${response}`)
                    })
                    .catch(error => {
                        console.log(`Unable to create event candidates: ${error}`)
                    })
            },
            onSelectTarget(row, event) {
                if (event === true) {
                    // add target to this.selectedTargets
                    if (!_.includes(this.selectedTargets, row.item.id)) this.selectedTargets.push(row.item.id);
                } else {
                    // remove target from this.selectedTargets
                    this.selectedTargets = this.selectedTargets.filter(function(value){
                        return value != row.item.id;
                    });
                }
            }
        }
    }
</script>
