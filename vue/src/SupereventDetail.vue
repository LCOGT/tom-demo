<template>
  <div>
    <div>
      <b-alert v-for="message in messages" :key="message" show>
        {{ message }}
      </b-alert>
      <b-alert :show="showCreatedCandidatesMessage" dismissable>{{
        this.createdCandidatesMessage
      }}</b-alert>
    </div>
    <gravitational-wave-banner :supereventData="superevent_data" />
    <b-row>
      <b-col cols="8">
        <alerts-table
          :alerts="alerts"
          @selected-alert="onSelectAlert"
        ></alerts-table>
      </b-col>
      <b-col cols="4">
        <b-row>
          <b-img
            :src="getBayestarImageUrl(this.superevent_identifier, 'bayestar.volume.png')"
            fluid
          ></b-img>
        </b-row>
        <b-row>
          <b-img
            :src="getBayestarImageUrl(this.superevent_identifier, 'bayestar.png')"
            fluid
          ></b-img>
        </b-row>
      </b-col>
    </b-row>
    <b-row class="my-3">
      <b-col class="col-md-auto">
        <add-candidate-modal
          :supereventId="this.superevent_id"
          :existingEventCandidates="this.eventCandidates"
          @created-candidates="onCreatedCandidates"
        />
      </b-col>
      <b-col class="col-md-auto">
        <create-target-modal
          :alerts="this.selectedAlerts"
          :supereventId="this.superevent_id"
          @created-target-candidates="onCreatedCandidates"
        />
      </b-col>
    </b-row>
    <hr />
    <b-row>
      <b-col cols="12">
        <h3>Active Candidates</h3>
        <candidate-target-table
          :candidates="this.viableCandidates"
          @toggle-viability="onToggleViability"
          @change-priority="onChangePriority"
        />
      </b-col>
    </b-row>
    <b-row>
      <b-col cols="12">
        <h3>Retired Candidates</h3>
        <candidate-target-table
          :candidates="this.nonViableCandidates"
          @toggle-viability="onToggleViability"
          @change-priority="onChangePriority"
        />
      </b-col>
    </b-row>
    <hr />
  </div>
</template>

<script>
import axios from "axios";
import _ from "lodash";
import {
  AddCandidateModal,
  AlertsTable,
  CreateTargetModal,
  GravitationalWaveBanner,
  CandidateTargetTable,
} from "@/components";

export default {
  name: "SupereventDetail",
  components: {
    AddCandidateModal,
    AlertsTable,
    CreateTargetModal,
    CandidateTargetTable,
    GravitationalWaveBanner,
  },
  data: function () {
    return {
      alerts: [],
      alert_fields: [
        { key: "identifier" },
        { key: "timestamp", sortable: true },
        { key: "from" },
        { key: "subject" },
      ],
      messages: [],
      eventCandidates: [],
      selectedAlerts: [],
      superevent_identifier: undefined,
      superevent_data: {},
    };
  },
  computed: {
    viableCandidates() {
      return this.eventCandidates.filter((item) => {
        return item.viable;
      });
    },
    nonViableCandidates() {
      return this.eventCandidates.filter((item) => {
        return !item.viable;
      });
    },
  },
  props: {},
  mounted() {
    console.log("mounted SupereventDetail.vue");
    this.superevent_id = window.location.pathname
      .split("/")
      .filter((x) => x)[1]; // primary key of superevent record
    this.superevent_identifier = document.getElementById(
      "superevent_identifier"
    ).textContent; // identifier of superevent record
    this.getSupereventData();
    this.getGraceDBData();
  },
  methods: {
    getSupereventData() {
      // set this.eventCandidates
      let oldEventCandidates = this.eventCandidates.slice();
      this.eventCandidates = [];
      // retrieve the superevent data from the REST API
      axios
        .get(
          `${this.$store.state.tomApiBaseUrl}/api/superevents/${this.superevent_id}`
        )
        .then((response) => {
          response["data"]["event_candidates"].forEach((event_candidate) => {
            this.eventCandidates.push(event_candidate);
          });
          console.log(`getSupereventData: superevent event_candidates updated`);
        })
        .catch((error) => {
          console.log(
            `getSupereventData: Error getting database data for ${this.superevent_id}: ${error}`
          );
          this.eventCandidates = oldEventCandidates;
        });
    },
    getGraceDBData() {
      // set this.superevent_data
      // set this.alerts
      axios
        .get(
          `${this.$store.state.skipApiBaseUrl}/api/events/?identifier=${this.superevent_identifier}`,
          this.$store.state.skipAxiosConfig
        )
        .then((response) => {
          this.superevent_data = response["data"]["results"][0];
          axios
            .get(
              `${this.$store.state.skipApiBaseUrl}/api/events/${response["data"]["results"][0]["id"]}`,
              this.$store.state.skipAxiosConfig
            )
            .then((alert_response) => {
              this.alerts = alert_response["data"]["alerts"];
            })
            .catch((error) => {
              console.log(
                `Error getting alerts for superevent ${this.superevent_identifier}: ${error}`
              );
            });
        })
        .catch((error) => {
          console.log(
            `Error getting details for superevent ${this.superevent_identifier}: ${error}`
          );
        });
    },
    getBayestarImageUrl(superevent_identifier, image_filename) {
        // Construct URL with supplied argurments
        // for example: https://gracedb.ligo.org/api/superevents/S190426c/files/bayestar.volume.png"
          let url = 'https://gracedb.ligo.org/api/superevents/'
                    + superevent_identifier
                    + '/files/'
                    + image_filename;
          //console.log('getBayestarImageUrl: ' + url);
          return url;
    },
    onCreatedCandidates(count) {
      this.messages.push(`Successfully added ${count} candidates.`);
      this.getSupereventData();
    },
    onSelectAlert(row, event) {
      // TODO: move to a utils.js
      if (event === true) {
        // add target to list
        if (!_.includes(this.selectedAlerts, row.item))
          this.selectedAlerts.push(row.item);
      } else {
        // remove target from list
        this.selectedAlerts = this.selectedAlerts.filter(function (value) {
          return value !== row.item;
        });
      }
    },
    onToggleViability(row, event) {
      const event_candidate = row.item;  // it's table of event_candidates, so row.items are event_candidates
      const url = `${this.$store.state.tomApiBaseUrl}/api/eventcandidates/${event_candidate.id}/`;
      const new_viablility = !event_candidate.viable;
      const patch = { viable: new_viablility };  // construct the payload for the PATCH request

      axios  // make the PATCH request
        .patch(url, patch) // patch only serializes/validates/updates the fields in the Request Body
        .then((response) => {
          // if successful, update the front-end value with (new) data from the PATCH response
          row.item.viable = response['data'].viable; 
        })
        .catch((error) => {
          console.error('onToggleViability - url: ' + url);
          console.error('onToggleViability - patch: ' + JSON.stringify(patch));
          console.error(
            `onToggleViability: Error getting database data for ${JSON.stringify(event_candidate)}: ${error}`
          );
        });
    },
    onChangePriority(row, event) {
        //
        // TODO: at the moment, this isn't working. The b-table sorting seems to be interfering with
        // the v-model binding to the row.item.priority field, and maybe more problems with v-model binding
        // to the proper data.
        //
        const candidate = row.item;  // it's table of event_candidates, so row.items are event_candidates
        const url = `${this.$store.state.tomApiBaseUrl}/api/eventcandidates/${candidate.id}`;
        const new_priority = event;  // event is an integer for b-form-spinbutton
        const patch = { priority: new_priority };  // construct the payload for the PATCH request

        console.log('onChangePriority -        row.item.id: ' + row.item.id);
        console.log('onChangePriority -  row.item.priority: ' + row.item.priority);
        console.log('onChangePriority - candidate.priority: ' + candidate.priority);
        console.log('onChangePriority -              event: ' + event);

        axios  // make the PATCH request
            .patch(url, patch) // patch only serializes/validates/updates the fields in the Request Body
            .then((response) => {
                // if successful, update the front-end value with (new) data from the PATCH response
                //row.item.priority = response['data'].priority; 
            })
            .catch((error) => {
                console.error('onChangePriority - url: ' + url);
                console.error('onChangePriority - patch: ' + JSON.stringify(patch));
                console.error(
                    `onChangePriority: Error getting database data for ${JSON.stringify(candidate)}: ${error}`
                );
            });
        console.log('after PATCH...');
        console.log('onChangePriority - candidate.priority: ' + candidate.priority);
        console.log('onChangePriority -              event: ' + event);
        console.log();
    },
  },
};
</script>

<style scoped>
</style>