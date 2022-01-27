<template>
    <b-container>
        <b-table
            striped
            :primary-key="id"
            :sort-by="priority"
            :fields="candidateFields"
            :items="candidates">
            <!-- see https://bootstrap-vue.org/docs/components/table#custom-data-rendering -->

            <!-- Set up the link to the TargetDetail page for this Candidates Target -->
            <template #cell(target-link)="row">
                <b-link :href="getTargetDetailUrl(row.item.target)">{{ row.item.target.name }}</b-link>
            </template>

            <!-- Set up the Activate/Retire Button -->
            <template #cell(active)="row">
                <b-button size="sm" @click="$emit('toggle-viability', row, $event)">
                    {{ row.item.viable ? 'Retire' : 'Activate'}}
                </b-button>
            </template>

            <!-- Set up Priority (NOT IMPLEMENTED AT THE MOMENT)
            <template #cell(priority)="row">
                <b-form-spinbutton
                    inline
                    size="sm"
                    v-model="row.item.priority"
                @change="$emit('change-priority', row, $event)" />
            </template>
            -->

        </b-table>
    </b-container>
</template>

<script>
export default {
    name: 'CandidateTargetTable',
    components: {},
    props: {
      candidates: {
        type: Array,
        required: true
      },
    },
    computed: {
    },
    data() {
        return {
            candidateFields: [
                //{ 'key': 'priority', 'label': 'Priority', 'sortable': true },
                { 'key': 'target-link', 'label': 'Candidate', 'sortable': true },
                { 'key': 'superevent', 'label': 'Superevent', 'sortable': true },
                { 'key': 'superevent.note', 'label': 'Note' },
                { 'key': 'target.ra', 'label': 'RA', formatter: (value, key, item) => value.toLocaleString() },
                { 'key': 'target.dec', 'label': 'DEC', formatter: (value, key, item) => value.toLocaleString() },
                { 'key': 'active' },
            ],
        }
    },
    methods: {
        getTargetDetailUrl(target) {
            // get the base url from the vuex store and append to it
            return `${this.$store.state.tomApiBaseUrl}/targets/${target.id}`;
        }
    }
}
</script>
