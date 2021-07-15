<template>
  <div id="target-list">
    <img alt="Vue logo" src="@/assets/logo.png">
    <ttk-target-table :targets="targets">
    </ttk-target-table>
  </div>
</template>

<script>
import { TTKMixin } from 'tom-toolkit-component-lib';

export default {
  name: 'TargetList',
  components: {
  },
  mixins: [TTKMixin.getDataMixin],
  data() {
    return {
      targets: [],
    };
  },
  props: {
    tomApiBaseUrl: {
      type: String,
      required: true
    }
  },
  methods: {
    // these methods override stubs in the getDataMixin
    initializeDataEndpoint: function() {
      return this.tomApiBaseUrl + '/api/targets/';
    },
    onSuccessfulRetrieval: function(response) {
      // extract the target data from the reponse
      this.targets = response['data']['results'];
      return response; // like overridden method in getDataMixin
    },
  }
}
</script>

<style>
#target-list {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
