import axios from 'axios';
import Vue from 'vue'
import Vuex from 'vuex';
import storePlugin from "./vuex/vuex_store_as_plugin";
import SupereventDetail from './SupereventDetail.vue'
import { BootstrapVue, BootstrapVueIcons } from 'bootstrap-vue';
import { TOMToolkitComponentLib } from 'tom-toolkit-component-lib';
import 'bootstrap/dist/css/bootstrap.css'  // This line and the following is necessary to get bootstrap working
import 'bootstrap-vue/dist/bootstrap-vue.css'

Vue.use(BootstrapVue);  // TODO: document the need to do this
Vue.use(BootstrapVueIcons);  // TODO: document icons as well
Vue.use(TOMToolkitComponentLib);
Vue.use(Vuex);
Vue.use(storePlugin);

Vue.config.productionTip = false

axios
  .get('/static/urls.json')
  .then(response => {
    new Vue({
      render: h => h(SupereventDetail, 
        {
          props: {
            tomApiBaseUrl: response['data']['tomDemoApiUrl'],
            skipApiBaseUrl: 'http://skip.dev.hop.scimma.org'
          }
        }
      ),
    }).$mount('#superevent-detail')
  })
  .catch(() => {
    console.log('Error getting URL configuration');
  });
