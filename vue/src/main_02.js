import Vue from 'vue'
import App02 from './App02.vue'
import axios from 'axios';
import BootstrapVue from 'bootstrap-vue';  // TODO: document all of this
import { TOMToolkitComponentLib } from 'tom-toolkit-component-lib';
import 'bootstrap/dist/css/bootstrap.css'  // This line and the following is necessary to get bootstrap working
import 'bootstrap-vue/dist/bootstrap-vue.css'

Vue.use(BootstrapVue);  // TODO: document the need to do this
Vue.use(TOMToolkitComponentLib);

Vue.config.productionTip = false

new Vue({
  render: h => h(App02),
}).$mount('#app')
