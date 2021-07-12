<template>
  <div id="app02">
    <img alt="Vue logo" src="./assets/logo.png">
    <ttk-target-table :tomApiEndpoint="tomApiEndpoint"></ttk-target-table>
  </div>
</template>

<script>
import axios from 'axios';
// import HelloWorld from './components/HelloWorld.vue'

export default {
  name: 'App02',
  components: {
    // HelloWorld
  },
  data() {
    return {
      tomApiEndpoint: "test"
    }
  },
  mounted() {
    axios
      .get('/static/urls.json')
      .then(response => {
        console.log('then');
        console.log(response);
        console.log('tomApiEndpoint');
        console.log(this.tomApiEndpoint);
        this.tomApiEndpoint = response['data']['tomDemoApiUrl'];
        console.log(this.tomApiEndpoint);
      })
      .catch(
        error => {
          console.log('error');
          console.log(error);
        }
      );
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
