<template>
  <div id="app02">
    <img alt="Vue logo" src="./assets/logo.png">
    <ttk-target-table :targets="data">
    </ttk-target-table>
  </div>
</template>

<script>
import axios from 'axios';
import { TTKMixin } from 'tom-toolkit-component-lib';
// import HelloWorld from './components/HelloWorld.vue'

export default {
  name: 'App02',
  components: {
    // HelloWorld
  },
  mixins: [TTKMixin.getDataMixin],

  data() {
    return {
      data: this.targets
    };
  },

  created() {
    console.log("App02.created: BEGIN");
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
    this.tomApiEndpoint = 'http://tom-demo-dev.lco.gtn';

    console.log("App02.created: END");
  },
  
  methods: {
    initializeDataEndpoint: function() {
      this.tomApiEndpoint = 'http://tom-demo-dev.lco.gtn'; // TODO: Arrrrrgggggghhhhhh !!!!
      console.log("initializeDataEndpoint to " + this.tomApiEndpoint)
      return this.tomApiEndpoint + '/api/targets/';
    },
    onSuccessfulRetrieval: function(response) {
      console.log("onSuccessfullRetrieval: BEGIN");
      this.targets = response['data']['results'];
      //console.log("targets: " + this.targets);
      console.log("onSuccessfullRetrieval: END");
      return response; // just like overridden method in super
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
