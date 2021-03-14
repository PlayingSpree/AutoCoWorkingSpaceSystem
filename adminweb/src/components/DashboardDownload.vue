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
      <v-spacer></v-spacer>
      <v-btn outlined
        ><v-icon class="mr-1" small>mdi-download</v-icon> ดาวน์โหลดข้อมูล</v-btn
      >
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
    range: []
  },
  data: function() {
    return {
      menu: false,
      shortcut: [
        {
          text: "today",
          onClick: () => {
            const date = [new Date(), new Date()];
            this.range = date;
          }
        },
        {
          text: "7 days",
          onClick: () => {
            const date = [
              new Date(Date.now() - 6 * 24 * 60 * 60 * 1000),
              new Date()
            ];
            this.range = date;
          }
        },
        {
          text: "30 days",
          onClick: () => {
            const date = [
              new Date(Date.now() - 29 * 24 * 60 * 60 * 1000),
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
      this.$emit("getnewdate", this.range);
    }
  }
};
</script>
