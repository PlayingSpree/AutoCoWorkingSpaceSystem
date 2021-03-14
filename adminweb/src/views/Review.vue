<template>
  <v-container>
    <review-chart />
    <review-table />
  </v-container>
</template>

<script>
import ReviewChart from "../components/ReviewChart.vue";
import ReviewTable from "../components/ReviewTable.vue";

export default {
  name: "review",
  components: {
    ReviewChart,
    ReviewTable
  }
};
</script>
