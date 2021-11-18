<template>
    <div>
        <div>
            <b-alert v-for="message in messages" :key="message" show>
                {{ message }}
            </b-alert>
            <b-alert :show="showCreatedCandidatesMessage" dismissable>{{ this.createdCandidatesMessage }}</b-alert>
        </div>
        <gravitational-wave-banner :supereventData="superevent_data" />
        <b-row>
            <b-col cols="8">
                <alerts-table :alerts="alerts" @selected-alert="onSelectAlert"></alerts-table>
            </b-col>
            <b-col cols="4">
                <b-row>
                    <b-img src="https://gracedb.ligo.org/api/superevents/S190426c/files/bayestar.volume.png" fluid></b-img>
                </b-row>
                <b-row>
                    <b-img src="https://gracedb.ligo.org/api/superevents/S190426c/files/bayestar.png" fluid></b-img>
                </b-row>
            </b-col>
        </b-row>
        <b-row class="my-3">
            <b-col class="col-md-auto">
                <add-candidate-modal :supereventId="this.superevent_id" :existingEventCandidates="this.eventCandidates" @created-candidates="onCreatedCandidates" />
            </b-col>
            <b-col class="col-md-auto">
                <create-target-modal :alerts="this.selectedAlerts" :supereventId="this.superevent_id" @created-target-candidates="onCreatedCandidates" />
            </b-col>
        </b-row>
        <hr>
        <b-row>
            <b-col cols="12">
                <h3>Viable Candidates</h3>
                <candidate-target-table
                  :candidates="this.eventCandidates"
                  :showViable="true"
                  @toggle-viability="onToggleViability" />
            </b-col>
        </b-row>
        <b-row>
            <b-col cols="12">
                <h3>Retired Candidates</h3>
                <candidate-target-table
                  :candidates="this.eventCandidates"
                  :showViable="false"
                  @toggle-viability="onToggleViability" />
            </b-col>
        </b-row>
    </div>
</template>

<script>
import axios from 'axios';
import _ from 'lodash';
import { AddCandidateModal, AlertsTable, CreateTargetModal,
         GravitationalWaveBanner,
         //SelectableTargetTable,
         CandidateTargetTable
         } from '@/components';
//import TargetList from './views/TargetList.vue';

export default {
    name: 'SupereventDetail',
    components: {
        AddCandidateModal,
        AlertsTable,
        CreateTargetModal,
        CandidateTargetTable,
        GravitationalWaveBanner,
        //SelectableTargetTable,
        //TargetList,
    },
    data: function() {
        return {
            alerts: [],
            alert_fields: [
                { 'key': 'identifier' },
                { 'key': 'timestamp', 'sortable': true },
                { 'key': 'from' },
                { 'key': 'subject' }
            ],
            messages: [],
            eventCandidates: [],
            selectedAlerts: [],
            superevent_identifier: undefined,
            superevent_data: {}
        }
    },
    props: {
    },
    mounted() {
        console.log('mounted SupereventDetail.vue');
        this.superevent_id = window.location.pathname.split('/').filter(x => x)[1];  // primary key of superevent record
        this.superevent_identifier = document.getElementById('superevent_identifier').textContent;  // identifier of superevent record
        this.getSupereventData();
        this.getGraceDBData();
    },
    methods: {
        getSupereventData() {
            let oldEventCandidates = this.eventCandidates.slice();
            this.eventCandidates = [];
            axios
                .get(`${this.$store.state.tomApiBaseUrl}/api/superevents/${this.superevent_id}`)
                .then(response => {
                    response['data']['event_candidates'].forEach(event_candidate => {
                        //this.eventCandidates.push(event_candidate['target']);
                        this.eventCandidates.push(event_candidate);
                    });
                })
                .catch(error => {
                    console.log(`Error getting database data for ${this.superevent_id}: ${error}`);
                    this.eventCandidates = oldEventCandidates;
                })
        },
        getGraceDBData() {
            axios
                .get(`${this.$store.state.skipApiBaseUrl}/api/events/?identifier=${this.superevent_identifier}`, this.$store.state.skipAxiosConfig)
                .then(response => {
                    this.superevent_data = response['data']['results'][0];
                    axios
                        .get(`${this.$store.state.skipApiBaseUrl}/api/events/${response['data']['results'][0]['id']}`, this.$store.state.skipAxiosConfig)
                        .then(alert_response => {
                            this.alerts = alert_response['data']['alerts'];
                        })
                        .catch(error => {
                            console.log(`Error getting alerts for superevent ${this.superevent_identifier}: ${error}`);
                        })
                })
                .catch(error => {
                    console.log(`Error getting details for superevent ${this.superevent_identifier}: ${error}`);
                })
        },
        onCreatedCandidates(count) {
            this.messages.push(`Successfully added ${count} candidates.`);
            this.getSupereventData();
        },
        onSelectAlert(row, event) {  // TODO: move to a utils.js
            if (event === true) {
                // add target to list
                if (!_.includes(this.selectedAlerts, row.item)) this.selectedAlerts.push(row.item);
            } else {
                // remove target from list
                this.selectedAlerts = this.selectedAlerts.filter(function(value){
                    return value !== row.item;
                });
            }
        },
        onToggleViability(row, event) {
            console.log('onToggleViability row: ' + row);
            console.log('onToggleViability event: ' + event);
        }
    }
}
</script>

<style scoped>

</style>