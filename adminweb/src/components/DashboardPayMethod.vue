<template>
  <v-card class="mt-5 pa-3">
    <v-container fluid>
      <v-row>
        <v-col cols="12"
          ><v-card-title style="font-size:20px">
            ช่องทางการชำระเงิน
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
                      :colors="['#689F38', '#1851b2']"
                      :data="pieData"
                      :legend="false"
                    ></pie-chart
                  ></v-col>
                  <v-col>
                    <p>
                      <v-icon style="color: #1851b2" small>mdi-circle</v-icon>
                      ชำระผ่านพร้อมเพย์
                    </p>
                    <p>{{ promptPercent() }} %</p>
                    <p>
                      <v-icon style="color: #689F38" small>mdi-circle</v-icon>
                      ชำระผ่านบัตรเครดิต
                    </p>
                    <p>{{ creditPercent() }} %</p>
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
                          รายการชำระทั้งหมด
                        </v-card-title>
                        <v-card-text> ฿ {{ allPay() }} </v-card-text>
                      </v-card>
                    </v-col>
                  </v-row>

                  <v-row>
                    <v-col cols="6" height="100%">
                      <v-card outlined style="border-color:#689F38">
                        <v-card-title style="font-size:1em">
                          บัตรเครดิต
                        </v-card-title>
                        <v-card-text> ฿ {{ pieData[0][1] }} </v-card-text>
                      </v-card>
                    </v-col>
                    <v-col cols="6" height="100%">
                      <v-card outlined style="border-color:#1851b2">
                        <v-card-title style="font-size:1em">
                          พร้อมเพย์
                        </v-card-title>
                        <v-card-text> ฿ {{ pieData[1][1] }} </v-card-text>
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
  data: function() {
    return {
      pieData: [
        ["ชำระผ่านบัตรเครดิต", 770],
        ["ชำระผ่านพร้อมเพย์", 230]
      ]
    };
  },

  methods: {
    creditPercent: function() {
      return (
        (this.pieData[0][1] / (this.pieData[0][1] + this.pieData[1][1])) *
        100
      ).toFixed(2);
    },

    promptPercent: function() {
      return (100 - this.creditPercent()).toFixed(2);
    },

    allPay: function() {
      return this.pieData[0][1] + this.pieData[1][1];
    }
  }
};
</script>
