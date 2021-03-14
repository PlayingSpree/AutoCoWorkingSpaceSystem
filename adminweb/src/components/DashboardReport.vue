<template>
  <v-card class="mt-5 pa-3">
    <v-container fluid>
      <v-row>
        <v-col cols="12"
          ><v-card-title style="font-size:20px">
            การรายงานปัญหา
          </v-card-title></v-col
        ></v-row
      >
      <v-row>
        <v-container fluid>
          <v-row>
            <v-col cols="6">
              <v-card outlined class="pa-3">
                <v-row class="align-center">
                  <v-col
                    ><pie-chart
                      :colors="['#C62828', '#FFA726']"
                      :data="pieData"
                      :legend="false"
                      :donut="true"
                    ></pie-chart
                  ></v-col>
                  <v-col>
                    <p>
                      <v-icon style="color: #FFA726" small>mdi-circle</v-icon>
                      ชำระผ่านพร้อมเพย์
                    </p>
                    <p>{{ elecPercent() }} %</p>
                    <p>
                      <v-icon style="color: #C62828" small>mdi-circle</v-icon>
                      ชำระผ่านบัตรเครดิต
                    </p>
                    <p>{{ appPercent() }} %</p>
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
                    <v-col cols="12">
                      <v-card outlined height="100%">
                        <v-card-title style="font-size:1em">
                          การรายงานปัญหาทั้งหมด
                        </v-card-title>
                        <v-card-text> {{ allReport() }} </v-card-text>
                      </v-card>
                    </v-col>
                  </v-row>

                  <v-row>
                    <v-col cols="6" height="100%">
                      <v-card outlined style="border-color:#C62828">
                        <v-card-title style="font-size:1em">
                          ปัญหาจากแอพพลิเคชั่น
                        </v-card-title>
                        <v-card-text> {{ pieData[0][1] }} </v-card-text>
                      </v-card>
                    </v-col>
                    <v-col cols="6" height="100%">
                      <v-card outlined style="border-color:#FFA726">
                        <v-card-title style="font-size:1em">
                          ปัญหาจากอุปกรณ์
                        </v-card-title>
                        <v-card-text> {{ pieData[1][1] }} </v-card-text>
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
export default {
  props: {
    range: []
  },
  data: function() {
    return {
      pieData: [
        ["แอพพลิเคชั่น", 4],
        ["อุปกรณ์", 1]
      ]
    };
  },

  methods: {
    appPercent: function() {
      return (
        (this.pieData[0][1] / (this.pieData[0][1] + this.pieData[1][1])) *
        100
      ).toFixed(2);
    },

    elecPercent: function() {
      return (100 - this.appPercent()).toFixed(2);
    },

    allReport: function() {
      return this.pieData[0][1] + this.pieData[1][1];
    }
  }
};
</script>
