<template>
  <v-card class="mt-5">
    <v-container fluid>
      <v-card-title style="font-size:20px">
        การเข้าใช้งาน
      </v-card-title>
      <v-container fluid>
        <v-row>
          <v-col cols="4">
            <v-card outlined style="border-color:#5E35B1">
              <v-card-title style="font-size:1em">
                การเข้าใช้ทั้งหมด
              </v-card-title>
              <v-card-text> {{ allaccesscount() }} </v-card-text>
            </v-card>
          </v-col>
          <v-col cols="4">
            <v-card outlined style="border-color:#303F9F">
              <v-card-title style="font-size:1em">
                Co-working space
              </v-card-title>
              <v-card-text> {{ coaccesscount() }} </v-card-text>
            </v-card>
          </v-col>
          <v-col cols="4">
            <v-card outlined style="border-color:#FFA726">
              <v-card-title style="font-size:1em">
                Meeting room
              </v-card-title>
              <v-card-text> {{ meetingaccesscount() }} </v-card-text>
            </v-card>
          </v-col>
        </v-row>
        <v-row>
          <v-col cols="12"
            ><v-card outlined>
              <line-chart
                :data="accessData"
                :colors="['#FFA726', '#303F9F']"
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
    this.getaccess();
    this.datearr = this.arrDate(this.range[0], this.range[1]);
  },

  data: function() {
    return {
      datearr: [],
      accessData: []
    };
  },

  watch: {
    range(val) {
      this.range[0] = val[0];
      this.range[1] = val[1];
      this.datearr = this.arrDate(this.range[0], this.range[1]);
      this.getaccess();
    }
  },

  methods: {
    async getaccess() {
      this.accessData = [];
      let allaccess = await axios.get(
        `iot/access/stat/?start=${this.range[0]
          .toISOString()
          .substr(0, 10)}&end=${this.range[1].toISOString().substr(0, 10)}`
      );
      let meetingaccess = allaccess.data.meetingroom_access_by_date;
      let coaccess = allaccess.data.coworkingspace_access_by_date;

      let meetingdata = {
        name: "Meeting room",
        data: {}
      };

      let codata = {
        name: "Co-working space",
        data: {}
      };

      for (let i = 0; i < this.datearr.length; i++) {
        meetingdata.data[this.datearr[i]] = 0;
        codata.data[this.datearr[i]] = 0;
      }

      for (let i = 0; i < meetingaccess.length; i++) {
        meetingdata.data[meetingaccess[i].date] = meetingaccess[i].count;
      }

      for (let i = 0; i < coaccess.length; i++) {
        codata.data[coaccess[i].date] = coaccess[i].count;
      }

      this.accessData.push(codata);
      this.accessData.push(meetingdata);

      console.log(this.accessData);
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

    meetingaccesscount() {
      const sum = Object.values(this.accessData[0].data).reduce(
        (a, b) => a + b
      );
      return sum;
    },

    coaccesscount() {
      const sum = Object.values(this.accessData[1].data).reduce(
        (a, b) => a + b
      );
      return sum;
    },

    allaccesscount() {
      return this.meetingaccesscount() + this.coaccesscount()
    }
  }
};
</script>
