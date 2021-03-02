<template>
  <v-container>
    <dashboard-download />
    <review-chart />
    <review-table />
  </v-container>
</template>

<script>
import DashboardDownload from "../components/DashboardDownload.vue";
import ReviewChart from "../components/ReviewChart.vue";
import ReviewTable from "../components/ReviewTable.vue";

export default {
  name: "review",
  components: {
    DashboardDownload,
    ReviewChart,
    ReviewTable
  }
};
</script>
