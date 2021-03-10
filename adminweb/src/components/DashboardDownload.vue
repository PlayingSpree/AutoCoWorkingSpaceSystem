<template>
  <v-card class="mt-5">
    <v-card-actions
      ><p class="my-auto mr-2">ระยะเวลาของข้อมูล</p>
      <date-picker
        v-model="range"
        lang="en"
        range
        type="date"
        format="YYYY-MM-DD"
        confirm
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
  data: function() {
    return {
      range: [new Date(Date.now() - 6 * 24 * 60 * 60 * 1000), new Date()],
      menu: false,
      shortcut: [
        {
          text: "today",
          onClick: () => {
            this.range = [new Date(), new Date()];
          }
        },
        {
          text: "7 days",
          onClick: () => {
            const date = new Date();
            date.setTime(date.getTime() - 3600 * 1000 * 24 * 6);
            this.range = [date, new Date()];
          }
        },
        {
          text: "30 days",
          onClick: () => {
            const date = new Date();
            date.setTime(date.getTime() - 3600 * 1000 * 24 * 29);
            this.range = [date, new Date()];
          }
        }
      ]
    };
  }
};
</script>
