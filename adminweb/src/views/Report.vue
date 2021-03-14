<template>
  <v-container>
    <report-chart />
    <report-table />
  </v-container>
</template>

<script>
import ReportChart from "../components/ReportChart.vue";
import ReportTable from "../components/ReportTable.vue";

export default {
  components: { ReportChart, ReportTable }
};
</script>
