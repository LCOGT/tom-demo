<template>
    <b-container>
        <b-table
            striped     
            :fields="candidateFields"
            :items="filteredCandidates">
            <!-- see https://bootstrap-vue.org/docs/components/table#custom-data-rendering -->

            <!-- A virtual column -->
            <template #cell(index)="row">
            {{ row.index }}
            </template>

            <template #cell(target-link)="row">
                <b-link :href="getTargetDetailUrl(row.item.target)">{{ row.item.target.name }}</b-link>
            </template>
                <b-form-checkbox @change="$emit('toggle-viability', row, $event)"
                :checked="true" />
            </template>
            <template #cell(priority)="row">
                <b-form-spinbutton v-model="priority_value" value=1
                @change="$emit('change-priority', row, $event)" />
            </template>
        </b-table>
    </b-container>
</template>

<script>
export default {
    name: 'CandidateTargetTable',
    components: {},
    props: {
      selectable: {
          type: Boolean,
          required: false,
          default: true
      },
      candidates: {
        type: Array,
        required: true
      },
      showViable: {
          type: Boolean,
          required: false,
          default: true
      }
    },
    computed: {
      filteredCandidates() {
          return this.candidates.filter(
              item => { return item.viable === this.showViable })
      }
    },
    data() {
        return {
            priority_value: 'priority',
            candidateFields: [
                { 'key': 'priority', 'label': 'Priority', 'sortable': true },
                { 'key': 'target-link', 'label': 'Candidate', 'sortable': true },
                'index',
                { 'key': 'id', 'label': 'Superevent ID' },
                { 'key': 'target.id', 'label': 'Target ID', 'sortable': true },
                { 'key': 'superevent.note', 'label': 'Note' },
                { 'key': 'superevent.plan', 'label': 'Plan' },
                { 'key': 'superevent.note_on_plan', 'label': 'Note on Plan' },
                { 'key': 'target.ra', 'label': 'RA' },
                { 'key': 'target.dec', 'label': 'DEC' },
                { 'key': 'viable' },
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
