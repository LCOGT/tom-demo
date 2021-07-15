import axios from 'axios';
import Vue from 'vue'
import SupereventDetail from './SupereventDetail.vue'
import BootstrapVue from 'bootstrap-vue';
import { TOMToolkitComponentLib } from 'tom-toolkit-component-lib';
import 'bootstrap/dist/css/bootstrap.css'  // This line and the following is necessary to get bootstrap working
import 'bootstrap-vue/dist/bootstrap-vue.css'

Vue.use(BootstrapVue);  // TODO: document the need to do this
Vue.use(TOMToolkitComponentLib);

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
