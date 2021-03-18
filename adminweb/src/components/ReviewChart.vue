<template>
  <v-card class="mt-5">
    <v-container fluid>
      <v-card-title style="font-size: 20px">
        คะแนนความพึงพอใจ
      </v-card-title>
      <v-container class="d-flex align-content-start flex-wrap">
        <v-card width="150px" height="100px" class="mr-2 mb-2" outlined>
          <v-card-title>
            คะแนนเฉลี่ย
          </v-card-title>
          <v-card-text>
            {{ avgScore() }}
          </v-card-text>
        </v-card>
        <v-card
          width="150px"
          height="100px"
          class="mr-2 mb-2"
          outlined
          style="border-color: #C62828"
          v-if="chartData[0].data['1'] != null"
        >
          <v-card-title>
            1 ดาว
          </v-card-title>
          <v-card-text>
            {{ chartData[0].data["1"] }}
          </v-card-text>
        </v-card>
        <v-card
          width="150px"
          height="100px"
          class="mr-2 mb-2"
          outlined
          style="border-color: #EF6C00"
          v-if="chartData[0].data['2'] != null"
        >
          <v-card-title>
            2 ดาว
          </v-card-title>
          <v-card-text>
            {{ chartData[0].data["2"] }}
          </v-card-text>
        </v-card>
        <v-card
          width="150px"
          height="100px"
          class="mr-2 mb-2"
          outlined
          style="border-color: #FDD835"
          v-if="chartData[0].data['3'] != null"
        >
          <v-card-title>
            3 ดาว
          </v-card-title>
          <v-card-text>
            {{ chartData[0].data["3"] }}
          </v-card-text>
        </v-card>
        <v-card
          width="150px"
          height="100px"
          class="mr-2 mb-2"
          outlined
          style="border-color: #76FF03"
          v-if="chartData[0].data['4'] != null"
        >
          <v-card-title>
            4 ดาว
          </v-card-title>
          <v-card-text>
            {{ chartData[0].data["4"] }}
          </v-card-text>
        </v-card>
        <v-card
          width="150px"
          height="100px"
          class="mr-2 mb-2"
          outlined
          style="border-color: #388E3C"
          v-if="chartData[0].data['5'] != null"
        >
          <v-card-title>
            5 ดาว
          </v-card-title>
          <v-card-text>
            {{ chartData[0].data["5"] }}
          </v-card-text>
        </v-card>
      </v-container>
      <bar-chart
        :data="chartData"
        :legend="false"
        :colors="[['#C62828', '#EF6C00', '#FDD835', '#76FF03', '#388E3C']]"
        suffix=" ครั้ง"
      ></bar-chart>
    </v-container>
  </v-card>
</template>

<script>
import axios from "axios";

export default {
  props: {
    range: [],
    datatowatch: []
  },
  data: function() {
    return {
      review: {},
      chartData: []
    };
  },

  created() {
    this.getReview();
  },

  watch: {
    range(val) {
      this.range[0] = val[0];
      this.range[1] = val[1];
      this.getReview();
    },

    datatowatch: {
      deep: true,
      handler() {
        this.getReview();
      }
    }
  },

  methods: {
    async getReview() {
      let enstar = [];

      for (let i in this.datatowatch) {
        if (this.datatowatch[i] == true) {
          enstar.push(i);
        }
      }

      var data = {
        name: "จำนวนครั้ง",
        data: {}
      };

      for (let i = 0; i < enstar.length; i++) {
        data.data[enstar[i]] = 0;
      }

      let review = await axios.get(
        `feedback/?start=${this.range[0]
          .toISOString()
          .substr(0, 10)}&end=${this.range[1].toISOString().substr(0, 10)}`
      );
      review = review.data;

      for (var i = 0; i < review.length; i++) {
        if (review[i].rating == 1) {
          if (data.data["1"] != null) {
            data.data["1"] += 1;
          }
        } else if (review[i].rating == 2) {
          if (data.data["2"] != null) {
            data.data["2"] += 1;
          }
        } else if (review[i].rating == 3) {
          if (data.data["3"] != null) {
            data.data["3"] += 1;
          }
        } else if (review[i].rating == 4) {
          if (data.data["4"] != null) {
            data.data["4"] += 1;
          }
        } else if (review[i].rating == 5) {
          if (data.data["5"] != null) {
            data.data["5"] += 1;
          }
        }
      }

      this.chartData = [];
      this.chartData.push(data);
    },

    avgScore: function() {
      let sum = 0;
      let count = 0;
      for (var i = 0; i < Object.keys(this.chartData[0].data).length; i++) {
        let counti = this.chartData[0].data[
          Object.keys(this.chartData[0].data)[i]
        ];
        let sumi = counti * Object.keys(this.chartData[0].data)[i];
        sum += sumi;
        count += counti;
      }
      let avg = (sum / count).toFixed(2);
      if (isNaN(avg)) {
        avg = 0;
      }
      return avg;
    }
  }
};
</script>
