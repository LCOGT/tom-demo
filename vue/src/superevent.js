import axios from 'axios';
import Vue from 'vue'
import Vuex from 'vuex';
import store from './vuex/vuex_store_as_plugin';
import SupereventDetail from './SupereventDetail.vue'
import { BootstrapVue, BootstrapVueIcons } from 'bootstrap-vue';
import { TOMToolkitComponentLib } from 'tom-toolkit-component-lib';
import 'bootstrap/dist/css/bootstrap.css'  // This line and the following is necessary to get bootstrap working
import 'bootstrap-vue/dist/bootstrap-vue.css'

Vue.use(BootstrapVue);  // TODO: document the need to do this
Vue.use(BootstrapVueIcons);  // TODO: document icons as well
Vue.use(TOMToolkitComponentLib);
Vue.use(Vuex);
Vue.use(store);

Vue.config.productionTip = false

axios.defaults.xsrfHeaderName = 'X-CSRFToken';
axios.defaults.xsrfCookieName = 'csrftoken';
axios.defaults.withCredentials = true;

axios
  .get('/static/urls.json')
  .then(response => {
    Vue.prototype.$store.commit('setTomApiBaseUrl', response['data']['tomDemoApiUrl']);
    Vue.prototype.$store.commit('setTomAxiosConfig', {xsrfHeaderName: 'x-csrftoken', xsrfCookieName: 'csrftoken', withCredentials: true});
    Vue.prototype.$store.commit('setSkipApiBaseUrl', 'http://skip.dev.hop.scimma.org');
    Vue.prototype.$store.commit('setSkipAxiosConfig', {withCredentials: false});
    new Vue({
      render: h => h(SupereventDetail, {}),
    }).$mount('#superevent-detail')
  })
  .catch(error => {
    console.log('Error getting URL configuration');
    console.log(error);
  });
