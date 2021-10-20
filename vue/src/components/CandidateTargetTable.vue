<template>
    <b-container>
        <b-table
            striped     
            :fields="candidateFields"
            :items="candidates">
            <template v-if="selectable === true" #cell(viable)="row">
                <b-form-checkbox @change="$emit('selected-target', row, $event)"
                checked=true />
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
    },
    data() {
        return {
            candidateFields: [
                { 'key': 'priority', 'label': 'Priority', 'sortable': true },
                { 'key': 'target.name', 'label': 'Candidate', 'sortable': true },
                { 'key': 'superevent.id', 'label': 'Reference' },
                { 'key': 'superevent.id', 'label': 'Discovery' },
                { 'key': 'target.id', 'label': 'Mag', 'sortable': true },
                { 'key': 'superevent.note', 'label': 'Note' },
                { 'key': 'superevent.plan', 'label': 'Plan' },
                { 'key': 'superevent.note_on_plan', 'label': 'Note on Plan' },
                { 'key': 'target.ra', 'label': 'RA' },
                { 'key': 'target.dec', 'label': 'DEC' },
                { 'key': 'viable' },
            ],
        }
    },
}
</script>
