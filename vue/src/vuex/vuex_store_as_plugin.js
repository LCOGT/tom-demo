import axios from 'axios';
import Vue from "vue/dist/vue.js";
import Vuex from "vuex";
import createPersistedState from "vuex-persistedstate";
import CounterModule from "./vuex_module_counter";

Vue.use(Vuex);
let plugins = [];
plugins.push(createPersistedState({
        // register here the state variable to be persisted throughout the users visit
        paths: ["counter.count",]
    }
));

let store = new Vuex.Store({
    state: {
        tomApiBaseUrl: 'http://localhost:8000',
        skipApiBaseUrl: 'http://skip.dev.hop.scimma.org',  // TODO: this should default to production whenever that exists
        tomAuthToken: '',
    },
    plugins: plugins,
    modules: {
        counter: CounterModule, // see @/vuex/vuex_counter_module.js
    },
    mutations: {
        setSkipApiBaseUrl(state, url) {
            state.skipApiBaseUrl = url;
        },
        setTomApiBaseUrl(state, url) {
            state.tomApiBaseUrl = url;
        }
    },
    actions: {
        getAuthenticationToken(credentials) {
            axios.post(
                `${state.tomApiBaseUrl}/api/token-auth/`,
                {username: credentials.username, password: credentials.password}
            )
            .then(response => {
                state.tomAuthToken = response.token;  // TODO: make this the actual value
            })
            .error(error => {
                console.log(`Unable to retrieve authentication token: ${error}`);
            });
        }
    },
    strict: process.env.NODE_ENV !== "production",
});

export default {
    store,
    install(Vue) { //resetting the default store to use this common store
        Vue.prototype.$store = store;
    }
}
