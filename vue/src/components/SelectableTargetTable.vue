<template>
    <b-container>
        <b-table
            :fields="targetFields"
            :items="targets">
            <template v-if="selectable === true" #cell(selected)="row">
                <b-form-checkbox @change="$emit('selected-target', row, $event)" />
            </template>
        </b-table>
    </b-container>
</template>

<script>
export default {
    name: 'SelectableTargetTable',
    components: {},
    props: {
      selectable: {
          type: Boolean,
          required: false,
          default: true
      },
      targets: {
        type: Array,
        required: true
      },
    },
    data() {
        return {
            targetFields: [
                { 'key': 'selected', 'label': '' },
                { 'key': 'name', 'sortable': true },
                { 'key': 'ra' },
                { 'key': 'dec' },
            ],
        }
    },
}
</script>
