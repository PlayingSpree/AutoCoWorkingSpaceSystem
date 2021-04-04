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
      <dashboard-download :range="datemain" @getnewdate="changedate" />
      <dashboard-main :range="datemain" />
      <dashboard-pay-method :range="datepaymethod" />
      <dashboard-user-overview :range="dateover" />
      <dashboard-report :range="datereport" />
      <dashboard-access :range="dateaccess" />
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
      datemain: [new Date(Date.now() - 24 * 60 * 60 * 1000), new Date()],
      datepaymethod: [new Date(Date.now() - 24 * 60 * 60 * 1000), new Date()],
      dateover: [new Date(Date.now() - 24 * 60 * 60 * 1000), new Date()],
      datereport: [new Date(Date.now() - 24 * 60 * 60 * 1000), new Date()],
      dateaccess: [new Date(Date.now() - 24 * 60 * 60 * 1000), new Date()],
    };
  },

  methods: {
    changedate(value) {
      this.datemain = value;
      this.datepaymethod = value;
      this.dateover = value;
      this.datereport = value;
      this.dateaccess = value;
    }
  }
};
</script>

<style></style>
