<template>
  <div id="dashboard">
    <v-container grid-list-xs>
      <v-row>
        <v-col cols="12">
          <h3>
            Business Insights
          </h3>
        </v-col>
      </v-row>
      <dashboard-download />
      <dashboard-main />
      <dashboard-pay-method/>
      <dashboard-user-overview/>
    </v-container>
  </div>
</template>

<script>
import DashboardMain from "../components/DashboardMain.vue";
import DashboardDownload from "../components/DashboardDownload.vue";
import DashboardPayMethod from "../components/DashboardPayMethod.vue"
import DashboardUserOverview from "../components/DashboardUserOverview.vue"

export default {
  name: "dashboard",
  components: {
    DashboardMain,
    DashboardDownload,
    DashboardPayMethod,
    DashboardUserOverview
  }
};
</script>

<style></style>
