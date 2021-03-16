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
        <v-card width="150px" height="100px" class="mr-2 mb-2" outlined>
          <v-card-title>
            1 ดาว
          </v-card-title>
          <v-card-text>
            {{ chartData[0].data["1 ดาว"] }}
          </v-card-text>
        </v-card>
        <v-card width="150px" height="100px" class="mr-2 mb-2" outlined>
          <v-card-title>
            2 ดาว
          </v-card-title>
          <v-card-text>
            {{ chartData[0].data["2 ดาว"] }}
          </v-card-text>
        </v-card>
        <v-card width="150px" height="100px" class="mr-2 mb-2" outlined>
          <v-card-title>
            3 ดาว
          </v-card-title>
          <v-card-text>
            {{ chartData[0].data["3 ดาว"] }}
          </v-card-text>
        </v-card>
        <v-card width="150px" height="100px" class="mr-2 mb-2" outlined>
          <v-card-title>
            4 ดาว
          </v-card-title>
          <v-card-text>
            {{ chartData[0].data["4 ดาว"] }}
          </v-card-text>
        </v-card>
        <v-card width="150px" height="100px" class="mr-2 mb-2" outlined>
          <v-card-title>
            5 ดาว
          </v-card-title>
          <v-card-text>
            {{ chartData[0].data["5 ดาว"] }}
          </v-card-text>
        </v-card>
      </v-container>
      <bar-chart
        :data="chartData"
        :legend="false"
        :colors="[['#C62828', '#EF6C00', '#FDD835', '#76FF03', '#388E3C']]"
      ></bar-chart>
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
    }
  },

  methods: {
    async getReview() {
      var data = {
        name: "จำนวนครั้ง",
        data: {
          "1 ดาว": 0,
          "2 ดาว": 0,
          "3 ดาว": 0,
          "4 ดาว": 0,
          "5 ดาว": 0
        }
      };
      let review = await axios.get(
        `feedback/?start=${this.range[0]
          .toISOString()
          .substr(0, 10)}&end=${this.range[1].toISOString().substr(0, 10)}`
      );
      review = review.data;

      for (var i = 0; i < review.length; i++) {
        if (review[i].rating == 1) {
          data.data["1 ดาว"] += 1;
        } else if (review[i].rating == 2) {
          data.data["2 ดาว"] += 1;
        } else if (review[i].rating == 3) {
          data.data["3 ดาว"] += 1;
        } else if (review[i].rating == 4) {
          data.data["4 ดาว"] += 1;
        } else if (review[i].rating == 5) {
          data.data["5 ดาว"] += 1;
        }
      }
      this.chartData = [];
      this.chartData.push(data);
    },

    avgScore: function() {
      var sum = 0;
      var count = 0;
      for (var i = 1; i < 6; i++) {
        var counti = this.chartData[0].data[`${i} ดาว`];
        var sumi = counti * i;
        sum += sumi;
        count += counti;
      }
      return (sum / count).toFixed(2);
    }
  }
};
</script>
