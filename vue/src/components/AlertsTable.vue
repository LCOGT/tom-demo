<template>
    <div>
        <b-form-group>
            <b-form-input id="filter-input" v-model="filter" type="search" placeholder="Search Alerts" />
        </b-form-group>
        <b-table
            id="alerts-table"
            sticky-header="600px"
            hover
            head-variant="light"
            foot-clone
            :filter="filter"
            :items="getAlertsFromAlertData()"
            :fields="alert_fields"
            @row-clicked="showRowDetails"
        >
            <template #cell(selected)="row">
                <div v-if="row.item.right_ascension !== null && row.item.declination !== null">
                    <b-form-checkbox @change="$emit('selected-alert', row, $event)" />
                </div>
            </template>
            <template #cell(show_details)="data">
                <b-link v-if="data.detailsShowing" @click="data.toggleDetails">
                    <b-icon-caret-down />
                </b-link>
                <b-link v-else @click="data.toggleDetails">
                    <b-icon-caret-right />
                </b-link>
            </template>
            <template #row-details="data">
                <span v-if="data.item.parsed_message.body !== undefined">{{ data.item.parsed_message.body }}</span>
            </template>
            <template #cell(identifier)="data">
                <b-link :href="getAlertUrl(data.value)">{{ data.value }}</b-link>
            </template>
            <template #cell(timestamp)="data">
                {{ getAlertDate(data) }}
            </template>
            <template #cell(from)="data">
                {{ data.item.parsed_message.from }}
            </template>
            <template #cell(subject)="data">
                {{ data.item.parsed_message.subject }}
            </template>
        </b-table>
    </div>
</template>

<script>
import moment from 'moment';

export default {
    name: 'AlertsTable',
    components: {},
    data: function() {
        return {
            alert_data: [],
            alert_fields: [
                { 'key': 'selected', 'label': '' },
                { 'key': 'show_details', 'label': '' },
                { 'key': 'identifier' },
                { 'key': 'timestamp', 'sortable': true },
                { 'key': 'from' },
                { 'key': 'subject' }
            ],
            filter: null,
        }
    },
    props: {
        alerts: {
            type: Array,
            required: true
        },
    },
    mounted() {
        console.log(this.alerts);
    },
    methods: {
        getAlertUrl(alert) {
            return `${this.$store.state.skipApiBaseUrl}/api/v2/alerts/${alert}`;
        },
        getAlertsFromAlertData() {
            return this.alerts.filter(alert => alert.parsed_message.title !== "GCN/LVC NOTICE");
        },
        getAlertDate(alert) {  // TODO: fix this
            return moment(alert.timestamp).format('YYYY-MM-DD hh:mm:ss');
        },
        showRowDetails(item, index, event) {
            item._showDetails = !item._showDetails;
        }
    }
}
</script>

<style scoped>
#alerts-table {
    height: 400px;
}
</style>