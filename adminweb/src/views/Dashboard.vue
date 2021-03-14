<template>
  <div id="dashboard">
    <v-container>
      <v-row>
        <v-col cols="12">
          <h3>
            Business Insights
          </h3>
        </v-col>
      </v-row>
      <dashboard-download :range="date" @getnewdate="changedate" />
      <dashboard-main :range="date" />
      <dashboard-pay-method :range="date" />
      <dashboard-user-overview :range="date" />
      <dashboard-report :range="date" />
      <dashboard-access :range="date" />
    </v-container>
  </div>
</template>

<script>
import DashboardMain from "../components/DashboardMain.vue";
import DashboardDownload from "../components/DashboardDownload.vue";
import DashboardPayMethod from "../components/DashboardPayMethod.vue";
import DashboardUserOverview from "../components/DashboardUserOverview.vue";
import DashboardReport from "../components/DashboardReport.vue";
import DashboardAccess from "../components/DashboardAccess.vue";

export default {
  name: "dashboard",
  components: {
    DashboardMain,
    DashboardDownload,
    DashboardPayMethod,
    DashboardUserOverview,
    DashboardReport,
    DashboardAccess
  },

  data: function() {
    return {
      date: [new Date(Date.now() - 24 * 60 * 60 * 1000), new Date()]
    };
  },

  methods: {
    changedate(value) {
      this.date = value;
    }
  }
};
</script>

<style></style>
