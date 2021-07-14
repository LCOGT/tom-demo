<template>
  <div id="app02">
    <img alt="Vue logo" src="./assets/logo.png">
    <ttk-target-table :targets="targets">
    </ttk-target-table>
  </div>
</template>

<script>
import axios from 'axios';
import { TTKMixin } from 'tom-toolkit-component-lib';

export default {
  name: 'App02',
  components: {
  },
  mixins: [TTKMixin.getDataMixin],

  data() {
    return {
      targets: [],
    };
  },

  created() {
    //console.log("App02.created: BEGIN");

    // TODO: the tomApiEndpoint should NOT be hard-coded like it
    // is here!! The problem is that the async axios call does
    // not return a value before initializeDataEndpoint gets called.
  
    // axios
    //   .get('/static/urls.json')
    //   .then(response => {
    //     console.log("BEFORE assignment -- this.tomApiEndpoint: " + this.tomApiEndpoint);
    //     this.tomApiEndpoint = response['data']['tomDemoApiUrl'];
    //     console.log("AFTER assignment -- this.tomApiEndpoint: " + this.tomApiEndpoint);
    //   })
    //   .catch(
    //     error => {
    //       console.log('App020.created.axios.catch ERROR');
    //       console.log(error);
    //     }
    //   );

    //console.log("App02.created: END");
  },
  
  methods: {
    // these methods override stubs in the getDataMixin
    initializeDataEndpoint: function() {
      // TODO: don't hard-code the tomApiEndpoint; get it from static/urls.json !!
      this.tomApiEndpoint = 'http://tom-demo-dev.lco.gtn';
      return this.tomApiEndpoint + '/api/targets/';
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
#app02 {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
