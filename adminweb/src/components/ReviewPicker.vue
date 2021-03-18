<template>
  <v-card class="mt-5">
    <v-card-actions
      ><p class="my-auto mr-2">ระยะเวลาของข้อมูล</p>
      <date-picker
        v-model="range"
        v-on:input="emitdate"
        lang="en"
        range
        type="date"
        format="YYYY-MM-DD"
        :confirm="true"
        :shortcuts="shortcut"
      ></date-picker>
      <p class="my-auto mx-2">ประเภทของข้อมูล</p>
      <v-btn @click="emitall" outlined :color="all ? 'red' : 'red lighten-4'"
        >ทั้งหมด</v-btn
      >
      <v-btn @click="emitstate(1)" outlined :color="datatowatch[1] ? 'white' : 'grey darken-2'">1 ดาว</v-btn>
      <v-btn @click="emitstate(2)" outlined :color="datatowatch[2] ? 'white' : 'grey darken-2'">2 ดาว</v-btn>
      <v-btn @click="emitstate(3)" outlined :color="datatowatch[3] ? 'white' : 'grey darken-2'">3 ดาว</v-btn>
      <v-btn @click="emitstate(4)" outlined :color="datatowatch[4] ? 'white' : 'grey darken-2'">4 ดาว</v-btn>
      <v-btn @click="emitstate(5)" outlined :color="datatowatch[5] ? 'white' : 'grey darken-2'">5 ดาว</v-btn>
    </v-card-actions>
  </v-card>
</template>

<script>
import DatePicker from "vue2-datepicker";
import "vue2-datepicker/index.css";

export default {
  components: {
    DatePicker
  },
  props: {
    range: [],
    datatowatch: {},
    all: null
  },
  data: function() {
    return {
      menu: false,
      shortcut: [
        {
          text: "24 hours",
          onClick: () => {
            const date = [new Date(Date.now() - 24 * 60 * 60 * 1000), new Date()];
            this.range = date;
          }
        },
        {
          text: "7 days",
          onClick: () => {
            const date = [
              new Date(Date.now() - 7 * 24 * 60 * 60 * 1000),
              new Date()
            ];
            this.range = date;
          }
        },
        {
          text: "30 days",
          onClick: () => {
            const date = [
              new Date(Date.now() - 30 * 24 * 60 * 60 * 1000),
              new Date()
            ];
            this.range = date;
          }
        }
      ]
    };
  },
  methods: {
    emitdate() {
      if (this.range[0].getHours() == 0) {
        this.range[0] = new Date(this.range[0].getTime() + 24 * 60 * 60 * 500);
        this.range[1] = new Date(this.range[1].getTime() + 24 * 60 * 60 * 500);
      }

      this.$emit("getnewdate", this.range);
    },

    emitall() {
        this.all = !this.all;
      
      if (this.all == true) {
        this.datatowatch[1] = true;
        this.datatowatch[2] = true;
        this.datatowatch[3] = true;
        this.datatowatch[4] = true;
        this.datatowatch[5] = true;
      } else {
        this.datatowatch[1] = false;
        this.datatowatch[2] = false;
        this.datatowatch[3] = false;
        this.datatowatch[4] = false;
        this.datatowatch[5] = false;
      }
      this.$emit("getallstate", this.all);
      this.$emit("getnewstate", this.datatowatch);
    },

    emitstate(state) {
      this.datatowatch[state] = !this.datatowatch[state];
      if (
        this.datatowatch[1] == false ||
        this.datatowatch[2] == false ||
        this.datatowatch[3] == false ||
        this.datatowatch[4] == false ||
        this.datatowatch[5] == false
      ) {
        this.all = false;
      }
      if (
        this.datatowatch[1] == true &&
        this.datatowatch[2] == true &&
        this.datatowatch[3] == true &&
        this.datatowatch[4] == true &&
        this.datatowatch[5] == true
      ) {
        this.all = true;
      }
      this.$emit("getallstate", this.all);
      this.$emit("getnewstate", this.datatowatch);
    }
  }
};
</script>
