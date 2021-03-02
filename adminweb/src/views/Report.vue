<template>
  <v-container>
    <dashboard-download />
    <report-chart />
    <report-table />
  </v-container>
</template>

<script>
import DashboardDownload from "../components/DashboardDownload.vue";
import ReportChart from "../components/ReportChart.vue";
import ReportTable from "../components/ReportTable.vue";

export default {
  components: { DashboardDownload, ReportChart, ReportTable }
};
</script>
