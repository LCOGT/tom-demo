 // this form of import (from vue/dist) required to share vuex store across componnets
import Vue from "vue/dist/vue.js";
import Vuex from "vuex";
import storePlugin from "./vuex/vuex_store_as_plugin";

import App from './App.vue';
import BootstrapVue from 'bootstrap-vue';

import SimpleCounter from "./components/SimpleCounter";

import { TOMToolkitComponentLib } from 'tom-toolkit-component-lib';
import 'bootstrap/dist/css/bootstrap.css'  // This line and the following is necessary to get bootstrap working
import 'bootstrap-vue/dist/bootstrap-vue.css'

Vue.use(BootstrapVue);  // TODO: document the need to do this
Vue.use(TOMToolkitComponentLib);
Vue.use(Vuex);
Vue.use(storePlugin);

Vue.config.productionTip = false

new Vue({
  render: h => h(App),
}).$mount('#app')

// TAKE NOTE of how components are mounted here:
// mounting components with el:/components: instead of render:/$mount
// allows capturing properties from HTML

new Vue({
  // not using render:/$mount
  el: "#simple_counter_a",
  components: {SimpleCounter}
});

new Vue({
    // not using render:/$mount
  el: "#simple_counter_b",
  components: {SimpleCounter}
});
