<template>
    <ttk-target-list :selectable="false" :tom-api-base-url="tomApiBaseUrl"></ttk-target-list>
</template>

<script>
export default {
    name: 'TargetListView',
    props: {
      tomApiBaseUrl: {
        type: String,
        required: true
      }
    }
}
</script>
