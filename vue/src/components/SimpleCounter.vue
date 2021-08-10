<template>
    <div class="counter">
        <h3>{{ msg }}</h3>
        <button @click="decrement">-</button>
        <span>   {{ count }}   </span>
        <button @click="increment">+</button>
    </div>
</template>

<script>
    export default {
        name: 'SimpleCounter',
        props: { msg: String },
        computed: {
            count() { return this.$store.state.counter.count }
        },
        methods: {
            increment() { this.$store.commit('increment') },
            decrement() { this.$store.commit('decrement') }
        },
    }
</script>

<style scoped>
    .hello { text-align: center; }
    .hello span {
        display: inline-block;
        min-width: 4em;
        margin: 1em;
    }
</style>