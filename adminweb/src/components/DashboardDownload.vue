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
          text: "24 hours",
          onClick: () => {
            const date = [
              new Date(Date.now() - 24 * 60 * 60 * 1000),
              new Date()
            ];
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
    }
  }
};
</script>
