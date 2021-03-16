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
                :curve="false"
                suffix=" บาท"
                thousands=","
              ></line-chart> </v-card
          ></v-col>
        </v-row>
      </v-container>
    </v-container>
  </v-card>
</template>

<script>
import axios from "axios";

export default {
  components: {},
  props: {
    range: []
  },
  created() {
    this.getpackagestat();
  },
  data: function() {
    return {
      datearr: [],
      chartData: []
    };
  },
  watch: {
    range(val) {
      this.range[0] = val[0];
      this.range[1] = val[1];
      this.getpackagestat();
    }
  },

  methods: {
    async getpackagestat() {
      let allstat = await axios.get(
        `payment/stat/?start=${this.range[0]
          .toISOString()
          .substr(0, 10)}&end=${this.range[1].toISOString().substr(0, 10)}`
      );
      this.chartData = [];
      var packagestat = allstat.data.coworkingspace_sale_by_date;
      var meetingstat = allstat.data.meetingroom_sale_by_date;
      this.datearr = this.arrDate(this.range[0], this.range[1]);

      var packdata = {
        name: "ยอดขายแพ็คเกจ",
        data: {}
      };

      var meetdata = {
        name: "ยอดจองห้องประชุม",
        data: {}
      };

      for (var i = 0; i < this.datearr.length; i++) {
        packdata.data[this.datearr[i]] = 0;
        meetdata.data[this.datearr[i]] = 0;
      }

      for (i = 0; i < packagestat.length; i++) {
        packdata.data[packagestat[i].date] = packagestat[i].amount / 100;
      }

      for (i = 0; i < meetingstat.length; i++) {
        meetdata.data[meetingstat[i].date] = meetingstat[i].amount / 100;
      }

      this.chartData.push(packdata);
      this.chartData.push(meetdata);
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

    packageIncome: function() {
      const sum = Object.values(this.chartData[0].data).reduce((a, b) => a + b);
      return sum;
    },

    meetingIncome: function() {
      const sum = Object.values(this.chartData[1].data).reduce((a, b) => a + b);
      return sum;
    },

    allIncome: function() {
      return this.packageIncome() + this.meetingIncome();
    }
  }
};
</script>
