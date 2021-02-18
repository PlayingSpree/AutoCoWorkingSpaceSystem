<template>
  <v-card class="mt-5">
    <v-container fluid>
      <v-card-title style="font-size:20px">
        ตัวชี้วัดหลัก
      </v-card-title>
      <v-container fluid>
        <v-row>
          <v-col cols="4">
            <v-card outlined>
              <v-card-title style="font-size:1em">
                ยอดขายทั้งหมด
              </v-card-title>
              <v-card-text> ฿ {{ allIncome() }} </v-card-text>
            </v-card>
          </v-col>
          <v-col cols="4">
            <v-card outlined style="border-color:#fa9056">
              <v-card-title style="font-size:1em">
                ยอดขายแพ็คเกจ
              </v-card-title>
              <v-card-text> ฿ {{ packageIncome() }} </v-card-text>
            </v-card>
          </v-col>
          <v-col cols="4">
            <v-card outlined style="border-color:#92c970">
              <v-card-title style="font-size:1em">
                ยอดจองห้องประชุม
              </v-card-title>
              <v-card-text> ฿ {{ meetingIncome() }} </v-card-text>
            </v-card>
          </v-col>
        </v-row>
        <v-row>
          <v-col cols="12"
            ><v-card outlined>
              <line-chart
                :data="chartData"
                :colors="['#fa9056', '#92c970']"
              ></line-chart> </v-card
          ></v-col>
        </v-row>
      </v-container>
    </v-container>
  </v-card>
</template>

<script>
export default {
  components: {},
  data: function() {
    return {
      chartData: [
        {
          name: "ยอดขายแพ็คเกจ",
          data: {
            "2020-02-8": 500,
            "2020-02-9": 1500,
            "2020-02-10": 1800,
            "2020-02-11": 0,
            "2020-02-12": 1700,
            "2020-02-13": 2500,
            "2020-02-14": 1000
          }
        },
        {
          name: "ยอดจองห้องประชุม",
          data: {
            "2020-02-8": 100,
            "2020-02-9": 1500,
            "2020-02-10": 1000,
            "2020-02-11": 3000,
            "2020-02-12": 1800,
            "2020-02-13": 1500,
            "2020-02-14": 2000
          }
        }
      ]
    };
  },

  methods: {
    packageIncome: function() {
      var sum = 0;
      for (var key in this.chartData[0].data) {
        sum += this.chartData[0].data[key];
      }
      return sum;
    },

    meetingIncome: function() {
      var sum = 0;
      for (var key in this.chartData[1].data) {
        sum += this.chartData[1].data[key];
      }
      return sum;
    },

    allIncome: function() {
      return this.packageIncome() + this.meetingIncome();
    }
  }
};
</script>
