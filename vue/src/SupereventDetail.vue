<template>
    <div>
        <b-jumbotron id="superevent-banner" class="py-4 pl-3 text-white">
            <b-row>
                <b-col cols="2">
                    <h1><span id="superevent_name">{{ superevent_id }}</span></h1>
                </b-col>
                <b-col cols="10">
                    <b-row>
                        <b-col>
                            <h3><span>Update {{ superevent_data.event_attributes[0].sequence_number }}</span></h3>
                        </b-col>
                        <b-col>
                            <h3><span>MassGap {{ superevent_data.event_attributes[0].attributes.prob_massgap }}</span></h3>
                        </b-col>
                        <b-col>
                            <h3><span>NSBH {{ superevent_data.event_attributes[0].attributes.prob_nsbh }}</span></h3>
                        </b-col>
                        <b-col>
                            <h3><span>90%: {{ superevent_data.event_attributes[0].attributes.area_90 }}</span></h3>
                        </b-col>
                        <b-col>
                            <h3><span>{{ superevent_data.event_attributes[0].attributes.Instruments }}</span></h3>
                        </b-col>
                        <b-col>
                            <h3><span>FAR {{ superevent_data.event_attributes[0].attributes.far }}</span></h3>
                        </b-col>
                    </b-row>
                    <b-row>
                        <b-col>
                            <h3><span>BNS {{ superevent_data.event_attributes[0].attributes.prob_bns }}</span></h3>
                        </b-col>
                        <b-col>
                            <h3><span>Terrestrial {{ superevent_data.event_attributes[0].attributes.prob_terres }}</span></h3>
                        </b-col>
                        <b-col>
                            <h3><span>BBH {{ superevent_data.event_attributes[0].attributes.prob_bbh }}</span></h3>
                        </b-col>
                        <b-col>
                            <h3><span>50%: {{ superevent_data.event_attributes[0].attributes.area_50 }}</span></h3>
                        </b-col>
                        <b-col>
                            <h3><span>{{ superevent_data.event_attributes[0].attributes.unknown_field }}</span></h3>
                        </b-col>
                        <b-col>
                            <h3><span>NS/Rem {{ superevent_data.event_attributes[0].attributes.prob_ns }}</span></h3>
                        </b-col>
                    </b-row>
                </b-col>
            </b-row>
        </b-jumbotron>
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
    </div>
</template>

<script>
import axios from 'axios';
import { AlertsTable } from '@/components';

export default {
    name: 'SupereventDetail',
    components: {
        AlertsTable
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
            superevent_id: undefined,
            superevent_data: {}
        }
    },
    props: {
        tomApiBaseUrl: {
            type: String,
            required: true
        },
        skipApiBaseUrl: {
            type: String,
            required: true
        }
    },
    mounted() {
        console.log('mounted');
        console.log(this.tomApiBaseUrl);
        console.log(this.skipApiBaseUrl);
        this.superevent_id = document.getElementById('superevent_id').textContent;
        axios
            .get(this.skipApiBaseUrl + '/api/events/?identifier=' + this.superevent_id)
            .then(response => {
                console.log(response);
                console.log(response['data']['results'][0]);
                this.superevent_data = response['data']['results'][0];
                axios
                    .get(this.skipApiBaseUrl + '/api/events/' + response['data']['results'][0]['id'])
                    .then(alert_response => {
                        console.log(alert_response)
                        this.alerts = alert_response['data']['alerts'];
                    })
                    .catch(
                        error => {
                            console.log(error);
                        }        
                    )
            })
            .catch(
                error => {
                    console.log(error);
                }
            )
    }
}
</script>

<style scoped>
#alerts-table {
    height: 400px;
}
#superevent-banner {
    width: 100%;
    background-color: #06345c;
}
span {
    color: white;
}
</style>