<template>
  <div id="app">
    <img alt="Vue logo" src="./assets/logo.png">
    <HelloWorld msg="This is the TOM Toolkit Vue.js Health Check Page"/>
  </div>
</template>

<script>
import HelloWorld from './components/HelloWorld.vue'
import axios from 'axios';

export default {
  name: 'App',
  components: {
    HelloWorld
  },
  mounted() {
      console.log('mounted');
      axios
          .get('/static/urls.json')
          .then(response => {
              console.log('then');
              console.log(response);
          })
          .catch(
              error => {
                console.log('error');
                console.log(error);
              }
          );
  }
}

// TODO: remove me
console.log("--------------------------------------------");
console.log(process.env.NODE_ENV);
console.log(process.env.VUE_APP_TOM_TOOLKIT_API_ROOT);
console.log(process.env.VUE_APP_SCIMMA_API_ROOT);
console.log(process.env.TOM_DEMO_TEST_API_URL);
console.log("--------------------------------------------");
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
