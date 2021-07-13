<template>
    <b-table id="alerts-table" sticky-header hover head-variant="light" foot-clone :items="getAlertsFromAlertData()" :fields="alert_fields">
        <template #cell(identifier)="data">
            <a href="{{ getAlertUrl(data.value) }}">{{ data.value }}</a>
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
    </b-table>
</template>

<script>

export default {
    name: 'AlertsTable',
    components: {},
    data: function() {
        return {
            alert_data: [],
            alert_fields: [
                { 'key': 'identifier' },
                { 'key': 'timestamp', 'sortable': true },
                { 'key': 'from' },
                { 'key': 'subject' }
            ],
        }
    },
    props: {
        alerts: {
            type: Array,
            required: true
        }
    },
    created() {
        console.log('alerts table');
    },
    methods: {
        getAlertUrl(alert) {
            console.log(alert);
            return ''
        },
        getAlertsFromAlertData() {
            console.log(this.alerts);
            return this.alerts;
        }
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