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
            <template #cell(selected)="data">
                <div v-if="data.item.right_ascension !== null && data.item.declination !== null">
                    <b-form-checkbox @change="$emit('selected-alert', data, $event)" />
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
                <div v-else-if="data.item.topic === 'lvc.lvc-counterpart'">
                    <dl class="row" v-for="[key, value] in Object.entries(data.item.parsed_message)" :key="[key, value]">
                        <dt class="col-md-3">{{ key }}: </dt>
                        <dd class="col-md-9">{{ value }}</dd>
                    </dl>
                </div>
            </template>
            <template #cell(identifier)="data">
                <b-link :href="getAlertUrl(data.item)">{{ data.value }}</b-link>
            </template>
            <template #cell(timestamp)="data">
                {{ getAlertDate(data.item) }}
            </template>
            <template #cell(from)="data">
                <span v-if="data.item.topic === 'gcn-circular'">
                    {{ getSimplifiedFromField(data.item.parsed_message.from) }}
                </span>
                <span v-else-if="data.item.topic === 'lvc.lvc-counterpart'">Swift-XRT Observation</span>
            </template>
            <template #cell(subject)="data">
                <span v-if="data.item.parsed_message.subject !== undefined">{{ data.item.parsed_message.subject }}</span>
                <span v-else-if="data.item.right_ascension !== undefined && data.item.declination !== undefined">
                    Right Ascension: {{ data.item.right_ascension_sexagesimal }}<br>
                    Declination: {{ data.item.declination_sexagesimal }}
                </span>
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
    },
    methods: {
        getAlertUrl(alert) {
            return `${this.$store.state.skipApiBaseUrl}/api/v2/alerts/${alert.id}`;
        },
        getAlertsFromAlertData() {
            return this.alerts.filter(alert => alert.parsed_message.title !== "GCN/LVC NOTICE");
        },
        getAlertDate(alert) {
            return moment(alert.timestamp).format('YYYY-MM-DD hh:mm:ss');
        },
        getSimplifiedFromField(from) {
            // remove <name@example.com> part of from field; leave name at Institution
            // split on the '<', take the first part, and trim the whitespace
            return from.split('<')[0].trim();
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