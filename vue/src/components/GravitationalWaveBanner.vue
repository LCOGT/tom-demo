<template>
    <div>
        <b-jumbotron id="superevent-banner" class="py-4 pl-3 text-white">
            <b-row>
                <b-col cols="2">
                    <h1><span id="superevent_name">{{ supereventData.identifier }}</span></h1>
                </b-col>
                <b-col cols="10">
                    <b-row>
                        <b-col>
                            <h3><span>Update {{ supereventData.event_attributes[0].sequence_number }}</span></h3>
                        </b-col>
                        <b-col>
                            <h3><span>MassGap {{ supereventData.event_attributes[0].attributes.prob_massgap }}</span></h3>
                        </b-col>
                        <b-col>
                            <h3><span>NSBH {{ supereventData.event_attributes[0].attributes.prob_nsbh }}</span></h3>
                        </b-col>
                        <b-col>
                            <h3><span>90%: {{ parseFloat(supereventData.event_attributes[0].attributes.area_90).toFixed(2) }}</span></h3>
                        </b-col>
                        <b-col>
                            <h3><span>{{ supereventData.event_attributes[0].attributes.Instruments }}</span></h3>
                        </b-col>
                        <b-col>
                            <h3><span>FAR {{ supereventData.event_attributes[0].attributes.far }}</span></h3>
                        </b-col>
                    </b-row>
                    <b-row>
                        <b-col>
                            <h3><span>BNS {{ supereventData.event_attributes[0].attributes.prob_bns }}</span></h3>
                        </b-col>
                        <b-col>
                            <h3><span>Terrestrial {{ supereventData.event_attributes[0].attributes.prob_terres }}</span></h3>
                        </b-col>
                        <b-col>
                            <h3><span>BBH {{ supereventData.event_attributes[0].attributes.prob_bbh }}</span></h3>
                        </b-col>
                        <b-col>
                            <h3><span>50%: {{ parseFloat(supereventData.event_attributes[0].attributes.area_50).toFixed(2) }}</span></h3>
                        </b-col>
                        <b-col>
                            <h3><span>{{ supereventData.event_attributes[0].attributes.unknown_field }}</span></h3>
                        </b-col>
                        <b-col>
                            <h3><span>NS/Rem {{ supereventData.event_attributes[0].attributes.prob_ns }}</span></h3>
                        </b-col>
                    </b-row>
                </b-col>
            </b-row>
        </b-jumbotron>
    </div>
</template>

<script>
export default {
    name: 'GravitationalWaveBanner',
    props: {
        supereventData: {
            type: Object,
            required: true
        }
    },
    mounted() {
        console.log('mounted GWB');
        console.log(this.supereventData);
    }
}
</script>

<style scoped>
#superevent-banner {
    width: 100%;
    background-color: #06345c;
}
span {
    color: white;
}
</style>