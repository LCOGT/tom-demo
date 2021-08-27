<template>
    <div>
        <div>
            <b-alert :show="showCreatedCandidatesMessage" dismissable>{{ this.createdCandidatesMessage }}</b-alert>
        </div>
        <gravitational-wave-banner :supereventData="superevent_data" />
        <b-row>
            <b-col cols="6">
                <alerts-table :alerts="alerts"></alerts-table>
            </b-col>
            <b-col cols="3">
                <b-img src="https://gracedb.ligo.org/api/superevents/S190426c/files/bayestar.volume.png" fluid></b-img>
            </b-col>
            <b-col cols="3">
                <b-img src="https://gracedb.ligo.org/api/superevents/S190426c/files/bayestar.png" fluid></b-img>
            </b-col>
        </b-row>
        <b-row class="my-3">
            <add-candidate-modal :supereventId="this.superevent_id" :existingEventCandidates="this.eventCandidates" @created-candidates="onCreatedCandidates" />
        </b-row>
        <b-row class="my-3">
            <b-col cols="6">
                <h3>Viable Candidates</h3>
                <selectable-target-table :targets="this.eventCandidates" />
            </b-col>
            <b-col cols="6">
                <h3>Retired Candidates</h3>
                <target-list :tomApiBaseUrl="this.$store.state.tomApiBaseUrl" />
            </b-col>
        </b-row>
    </div>
</template>

<script>
import axios from 'axios';
import { AddCandidateModal, AlertsTable, GravitationalWaveBanner, SelectableTargetTable } from '@/components';
import TargetList from './views/TargetList.vue';

export default {
    name: 'SupereventDetail',
    components: {
        AddCandidateModal,
        AlertsTable,
        GravitationalWaveBanner,
        SelectableTargetTable,
        TargetList,
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
            createdCandidatesMessage: '',
            eventCandidates: [],
            showCreatedCandidatesMessage: false,
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
                        this.eventCandidates.push(event_candidate['target']);
                    });
                    console.log(this.eventCandidates);
                })
                .catch(error => {
                    console.log(`Error getting database data for ${this.superevent_id}: ${error}`);
                    this.eventCandidates = oldEventCandidates;
                })
        },
        getGraceDBData() {
            axios
                .get(`${this.$store.state.skipApiBaseUrl}/api/events/?identifier=${this.superevent_identifier}`)
                .then(response => {
                    this.superevent_data = response['data']['results'][0];
                    console.log(this.superevent_data)
                    axios
                        .get(`${this.$store.state.skipApiBaseUrl}/api/events/${response['data']['results'][0]['id']}`)
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
        onCreatedCandidates(count) {  // TODO: get event candidates again to live update the page
            this.showCreatedCandidatesMessage = true;
            this.createdCandidatesMessage = `Successfully added ${count} candidates.`;
            this.getSupereventData();
        }
    }
}
</script>

<style scoped>

</style>