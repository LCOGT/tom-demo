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
    plugins: plugins,
    modules: {
        counter: CounterModule, // see @/vuex/vuex_counter_module.js
    },
    strict: process.env.NODE_ENV !== "production",
});

export default {
    store,
    install(Vue) { //resetting the default store to use this common store
        Vue.prototype.$store = store;
    }
}
