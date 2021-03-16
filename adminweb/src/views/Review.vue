<template>
  <v-container>
    <dashboard-download :range="date" @getnewdate="changedate" />
    <review-chart :range="date" />
    <review-table :range="date" />
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
