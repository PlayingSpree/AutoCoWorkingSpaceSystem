<template>
  <v-container>
    <dashboard-download :range="date" @getnewdate="changedate" />
    <report-chart :range="date" />
    <report-table :range="date" />
  </v-container>
</template>

<script>
import DashboardDownload from "../components/DashboardDownload.vue";
import ReportChart from "../components/ReportChart.vue";
import ReportTable from "../components/ReportTable.vue";

export default {
  name: "report",
  components: { DashboardDownload, ReportChart, ReportTable },

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
