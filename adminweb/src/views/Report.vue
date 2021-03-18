<template>
  <v-container>
    <report-date-picker :range="date" @getnewdate="changedate" />
    <report-chart :range="date" />
    <report-picker
      :datatowatch="towatch"
      :all="all"
      @getnewstate="changestate"
      @getallstate="changeallstate"
    />
    <report-table :range="date" :datatowatch="towatch" />
  </v-container>
</template>

<script>
import ReportChart from "../components/ReportChart.vue";
import ReportDatePicker from "../components/ReportDatePicker.vue";
import ReportPicker from "../components/ReportPicker.vue";
import ReportTable from "../components/ReportTable.vue";

export default {
  name: "report",
  components: { ReportChart, ReportTable, ReportPicker, ReportDatePicker },

  data: function() {
    return {
      date: [new Date(Date.now() - 24 * 60 * 60 * 1000), new Date()],
      towatch: {
        null: true,
        0: true,
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
