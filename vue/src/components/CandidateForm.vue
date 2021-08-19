<template>
    <div>
        <b-button v-b-modal.candidate-form-modal>Add Candidate</b-button>
        <b-modal id="candidate-form-modal">
            <b-form @submit="onCreateCandidate">
                <b-form-input id="target-name-input" v-model="form.name" placeholder="Target Name" @input="targetSearch" required />
                <b-form-input id="target-ra-input" v-model="form.ra" placeholder="Right Ascension" required />
                <b-form-input id="target-dec-input" v-model="form.dec" placeholder="Declination" required />
                <b-button type="submit" variant="primary">Submit</b-button>
            </b-form>
        </b-modal>
    </div>
</template>

<script>
    export default {
        data() {
            return {
                form: {
                    name: '',
                    ra: '',
                    dec: ''
                }
            }
        },
        methods: {
            targetSearch() {
                
            },
            onCreateCandidate(event) {
                event.preventDefault();
                console.log('submit');
            }
        }
    }
</script>
