<template>
  <v-container>
    <review-picker
      :range="date"
      :datatowatch="towatch"
      :all="all"
      @getnewstate="changestate"
      @getnewdate="changedate"
      @getallstate="changeallstate"
    />
    <review-chart :range="date" :datatowatch="towatch" :all="all" />
    <review-table :range="date" :datatowatch="towatch" :all="all" />
  </v-container>
</template>

<script>
import ReviewChart from "../components/ReviewChart.vue";
import ReviewPicker from "../components/ReviewPicker.vue";
import ReviewTable from "../components/ReviewTable.vue";

export default {
  name: "review",
  components: {
    ReviewChart,
    ReviewTable,
    ReviewPicker
  },

  data: function() {
    return {
      date: [new Date(Date.now() - 24 * 60 * 60 * 1000), new Date()],
      towatch: {
        1: true,
        2: true,
        3: true,
        4: true,
        5: true
      },
      all: true
    };
  },

  methods: {
    changedate(value) {
      this.date = value;
    },

    changestate(value) {
      this.towatch = value;
    },

    changeallstate(value) {
      this.all = value;
    }
  }
};
</script>
