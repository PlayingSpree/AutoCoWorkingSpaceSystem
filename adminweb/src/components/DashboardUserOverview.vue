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
                          จำนวนลูกค้าทั้งหมด
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
      pieData: []
    };
  },
  created() {
    this.getUserOverview();
  },

  watch: {
    range(val) {
      this.range[0] = val[0];
      this.range[1] = val[1];
      this.getUserOverview();
    }
  },

  methods: {
    async getUserOverview() {
      let allstat = await axios.get(
        `payment/stat/?start=${this.range[0]
          .toISOString()
          .substr(0, 10)}&end=${this.range[1].toISOString().substr(0, 10)}`
      );
      var piedata = [];

      var pienewuser = ["ลูกค้าใหม่", allstat.data.customer_new];
      var pieolduser = ["ลูกค้าเดิม", allstat.data.customer_old];

      piedata.push(pienewuser);
      piedata.push(pieolduser);
      this.pieData = piedata;
    },
    newPercent: function() {
      return (
        (this.pieData[0][1] / (this.pieData[0][1] + this.pieData[1][1])) *
        100
      ).toFixed(2);
    },

    oldPercent: function() {
      return (100 - this.newPercent()).toFixed(2);
    },

    allUser: function() {
      return this.pieData[0][1] + this.pieData[1][1];
    }
  }
};
</script>
