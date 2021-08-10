export default {
    state: {
        count: 0
    },
    // normally, Vuex Actions should change the state (not the mutators directly)
    mutations: {
        increment: state => state.count++,
        decrement: state => state.count--
    },
}