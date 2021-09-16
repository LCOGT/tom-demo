<template>
    <div>
        <b-button class="float-left" v-b-modal.candidate-from-target-modal variant="outline-primary">Add Candidates from Alerts</b-button>
        <b-modal id="candidate-from-target-modal" size="xl" title="Create Candidate(s) from Alerts">
            <!-- TODO: display targets to be created -->
            <b-container>
                <b-form @submit="onCandidateFromAlert">
                    <b-form-row>
                        <b-form-checkbox-group>
                            <b-form-checkbox v-for="group in userGroups" :key="group.name" :value="group.id">{{ group.name }}
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
    import axios from 'axios';

    export default {
        components: {
        },
        props: {
            alerts: {
                type: Array,
                required: false
            },
        },
        data() {
            return {
                userGroups: []
            }
        },
        mounted() {
            this.$root.$on('bv::modal::show', (bvEvent, modalId) => {
                axios  // WIP - get user groups and add them to form
                    .get(`${this.$store.state.tomApiBaseUrl}/api/groups/`, this.$store.state.tomAxiosConfig)
                    .then(response => {
                        console.log('groups');
                        console.log(response);
                        this.userGroups = response['data']['results'];
                    })
                    .catch(error => {
                        console.log(`Unable to retrieve groups: ${error}.`)
                    });
                });
        },
        methods: {
            onCandidateFromAlert() {  // TODO: require >1 candidate to select, possibly split into multiple events, also add form validation
            }
        }
    }
</script>