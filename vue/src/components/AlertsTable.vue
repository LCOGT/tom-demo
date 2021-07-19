<template>
    <div>
        <b-row>
            <b-form-group>
                <b-form-input id="filter-input" v-model="filter" type="search" placeholder="Search Alerts" />
            </b-form-group>
        </b-row>
        <b-table
            id="alerts-table"
            sticky-header
            hover
            head-variant="light"
            foot-clone
            :filter="filter"
            :items="getAlertsFromAlertData()"
            :fields="alert_fields"
        >
            <template #cell(show_details)="data">
                <b-link v-if="data.detailsShowing" @click="data.toggleDetails">
                    -
                </b-link>
                <b-link v-else @click="data.toggleDetails">
                    +
                </b-link>
            </template>
            <template #cell(identifier)="data">
                <b-link :href="getAlertUrl(data.value)">{{ data.value }}</b-link>
            </template>
            <!-- <template #cell(timestamp)="data">
                {{ data.identifier }}
            </template> -->
            <template #cell(from)="data">
                {{ data.item.parsed_message.from }}
            </template>
            <template #cell(subject)="data">
                {{ data.item.parsed_message.subject }}
            </template>
            <template #foot()="data">
                <span>{{ data.value }}</span>
            </template>
            <template #row-details="data">
                <span>{{ data.item.parsed_message.body }}</span>
            </template>
        </b-table>
    </div>
</template>

<script>

export default {
    name: 'AlertsTable',
    components: {},
    data: function() {
        return {
            alert_data: [],
            alert_fields: [
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
        skipApiBaseUrl: {
            type: String,
            required: true
        }
    },
    methods: {
        getAlertUrl(alert) {
            return `${this.skipApiBaseUrl}/api/v2/alerts/${alert}`;
        },
        getAlertsFromAlertData() {
            return this.alerts.filter(alert => alert.parsed_message.body !== undefined);
        }
    }
}
</script>

<style scoped>
#alerts-table {
    height: 400px;
}
</style>