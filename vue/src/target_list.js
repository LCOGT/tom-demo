import axios from 'axios';
import Vue from 'vue'
import TargetList from '@/views/TargetList.vue'
import BootstrapVue from 'bootstrap-vue';  // TODO: document all of this
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
      render: h => h(TargetList, 
        {
          props: {
            tomApiBaseUrl: response['data']['tomDemoApiUrl'],
          }
        }
      ),
    }).$mount('#target-list')
  })
  .catch(() => {
    console.log('Error getting URL configuration');
  });
