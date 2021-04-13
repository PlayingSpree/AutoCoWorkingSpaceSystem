<template>
  <v-card class="mt-5 pa-3">
    <v-container fluid>
      <v-row
        ><v-card-title style="font-size:20px">
          ภาพรวมผู้ซื้อ
        </v-card-title></v-row
      >
      <v-row>
        <v-container fluid>
          <v-row>
            <v-col cols="6">
              <v-card outlined class="pa-3">
                <v-row class="align-center">
                  <v-col
                    ><pie-chart
                      :colors="['#FF4081', '#80D8FF']"
                      :data="pieData"
                      :legend="false"
                      :donut="true"
                    ></pie-chart
                  ></v-col>
                  <v-col>
                    <p>
                      <v-icon style="color: #80D8FF" small>mdi-circle</v-icon>
                      ลูกค้าเดิม
                    </p>
                    <p>{{ oldPercent() }} %</p>
                    <p>
                      <v-icon style="color: #FF4081" small>mdi-circle</v-icon>
                      ลูกค้าใหม่
                    </p>
                    <p>{{ newPercent() }} %</p>
                  </v-col>
                </v-row>
              </v-card>
            </v-col>
            <v-col cols="6">
              <v-card
                class="align-center justify-center pa-3"
                height="100%"
                outlined
              >
                <v-container fluid fill-height>
                  <v-row>
                    <v-col cols="4" height="100%">
                      <v-card outlined>
                        <v-card-title style="font-size:1em">
                          ลูกค้าทั้งหมด
                        </v-card-title>
                        <v-card-text> {{ allUser() }} คน</v-card-text>
                      </v-card>
                    </v-col>
                    <v-col cols="4" height="100%">
                      <v-card outlined style="border-color:#80D8FF">
                        <v-card-title style="font-size:1em">
                          จำนวนลูกค้าเดิม
                        </v-card-title>
                        <v-card-text> {{ pieData[1][1] }} คน </v-card-text>
                      </v-card> </v-col
                    ><v-col cols="4" height="100%">
                      <v-card outlined style="border-color:#FF4081">
                        <v-card-title style="font-size:1em">
                          จำนวนลูกค้าใหม่
                        </v-card-title>
                        <v-card-text> {{ pieData[0][1] }} คน </v-card-text>
                      </v-card>
                    </v-col>
                  </v-row>
                  <v-row>
                    <v-col cols="12">
                      <v-card outlined height="100%">
                        <v-card-title style="font-size:1em">
                          ความพึงพอใจในการใช้บริการ
                        </v-card-title>
                        <v-card-text>
                          {{ avgScore() }}
                        </v-card-text>
                      </v-card>
                    </v-col>
                  </v-row>
                </v-container>
              </v-card>
            </v-col>
          </v-row>
        </v-container>
      </v-row>
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
      pieData: [],
      reviewdata: []
    };
  },
  created() {
    this.getUserOverview();
    this.getReview();
  },

  watch: {
    range(val) {
      this.range[0] = val[0];
      this.range[1] = val[1];
      this.getUserOverview();
      this.getReview();
    }
  },

  methods: {
    async getUserOverview() {
      let allstat = await axios.get(
        `payment/stat/?start=${this.range[0]
          .toISOString()
          .substr(0, 10)}&end=${this.range[1].toISOString().substr(0, 10)}`
      );
      let piedata = [];
      let pienewuser = ["ลูกค้าใหม่", 0];
      let pieolduser = ["ลูกค้าเดิม", 0];

      if (
        allstat.data.customer_new != null ||
        allstat.data.customer_old != null
      ) {
        pienewuser = ["ลูกค้าใหม่", allstat.data.customer_new];
        pieolduser = ["ลูกค้าเดิม", allstat.data.customer_old];
      }

      piedata.push(pienewuser);
      piedata.push(pieolduser);
      this.pieData = piedata;
    },
    newPercent: function() {
      let percent = (
        (this.pieData[0][1] / (this.pieData[0][1] + this.pieData[1][1])) *
        100
      ).toFixed(2);
      if (isNaN(percent)) {
        percent = 0;
      }
      return percent;
    },

    oldPercent: function() {
      let percent = (
        (this.pieData[1][1] / (this.pieData[0][1] + this.pieData[1][1])) *
        100
      ).toFixed(2);
      if (isNaN(percent)) {
        percent = 0;
      }
      return percent;
    },

    allUser: function() {
      return this.pieData[0][1] + this.pieData[1][1];
    },

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
      this.reviewdata = [];
      this.reviewdata.push(data);
    },

    avgScore: function() {
      let sum = 0;
      let count = 0;
      for (var i = 1; i < 6; i++) {
        let counti = this.reviewdata[0].data[`${i} ดาว`];
        let sumi = counti * i;
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
