import axios from 'axios';
import Vue from 'vue'
import BootstrapVue from 'bootstrap-vue';  // TODO: document all of this
import TargetListView from '@/views/TargetListView.vue'
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
      render: h => h(TargetListView,
        {
          props: {
            tomApiBaseUrl: response['data']['tomDemoApiUrl'],
          }
        }
      ),
    }).$mount('#target-list-view')
  })
  .catch(() => {
    console.log('Error getting URL configuration');
  });
