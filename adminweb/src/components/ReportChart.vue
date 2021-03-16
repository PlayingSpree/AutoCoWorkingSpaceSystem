<template>
  <v-card class="mt-5">
    <v-container fluid>
      <v-card-title class="font-size: 20px">
        การรายงานปัญหา
      </v-card-title>
      <v-container class="d-flex align-content-start flex-wrap">
        <v-card width="150px" height="150px" class="mr-2 mb-2" outlined>
          <v-card-title>
            ปัญหา
          </v-card-title>
          <v-card-text>
            {{ appReport() + itemReport() }}
          </v-card-text>
        </v-card>
        <v-card width="150px" height="150px" class="mr-2 mb-2" outlined style="border-color:#C62828">
          <v-card-title>
            แอพพลิเคชั่น
          </v-card-title>
          <v-card-text>
            {{ appReport() }}
          </v-card-text>
        </v-card>
        <v-card width="150px" height="150px" class="mr-2 mb-2" outlined style="border-color:#FFA726">
          <v-card-title>
            อุปกรณ์
          </v-card-title>
          <v-card-text>
            {{ itemReport() }}
          </v-card-text>
        </v-card>
      </v-container>
      <line-chart :colors="['#C62828', '#FFA726']" :curve="false" :data="chartData" />
    </v-container>
  </v-card>
</template>

<script>
import axios from "axios";

export default {
  props: {
    range: []
  },
  data: function() {
    return {
      datearr: [],
      chartData: []
    };
  },

  created() {
    this.getReportstat();
  },

  watch: {
    range(val) {
      this.range[0] = val[0];
      this.range[1] = val[1];
      this.getReportstat();
    }
  },

  methods: {
    async getReportstat() {
      let report = await axios.get(
        `feedback/problem/?start=${this.range[0]
          .toISOString()
          .substr(0, 10)}&end=${this.range[1].toISOString().substr(0, 10)}`
      );
      report = report.data;
      this.chartData = [];

      var appstat = {
        name: "แอพพลิเคชั่น",
        data: {}
      };

      var itemstat = {
        name: "อุปกรณ์",
        data: {}
      };

      this.datearr = this.arrDate(this.range[0], this.range[1]);

      for (let i = 0; i < this.datearr.length; i++) {
        appstat.data[this.datearr[i]] = 0;
        itemstat.data[this.datearr[i]] = 0;
      }
      
      for (let i = 0; i < report.length; i++) {
        if (report[i].type == 1) {
          appstat.data[report[i].date_created.substr(0, 10)] += 1;
        } else {
          itemstat.data[report[i].date_created.substr(0, 10)] += 1;
        }
      }

      this.chartData.push(appstat);
      this.chartData.push(itemstat);
    },

    arrDate(startDate, stopDate) {
      var datearray = [];
      var currentDate = startDate;
      while (currentDate <= stopDate) {
        datearray.push(currentDate.toISOString().substr(0, 10));
        currentDate = new Date(currentDate.setDate(currentDate.getDate() + 1));
      }
      return datearray;
    },

    appReport: function() {
      return Object.values(this.chartData[0].data).reduce((a, b) => a + b, 0);
    },

    itemReport: function() {
      return Object.values(this.chartData[1].data).reduce((a, b) => a + b, 0);
    }
  }
};
</script>
