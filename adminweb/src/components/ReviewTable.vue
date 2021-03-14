<template>
  <v-card class="mt-5">
    <v-card-title>
      รายละเอียดความพึงพอใจ
    </v-card-title>
    <v-card-title>
      <v-text-field
        v-model="search"
        append-icon="mdi-magnify"
        label="Search"
        single-line
        hide-details
      ></v-text-field>
    </v-card-title>
    <v-data-table :headers="headers" :items="review" :search="search">
    </v-data-table>
  </v-card>
</template>

<script>
import axios from "axios";

export default {
  data: function() {
    return {
      search: "",
      headers: [
        {
          text: "รหัส",
          align: "start",
          filterable: true,
          value: "id"
        },
        { text: "รายละเอียด", value: "text" },
        { text: "วันและเวลา", value: "date_created" },
        { text: "คะแนน", value: "rating" }
      ],
      review: []
    };
  },

  created() {
    this.getReview();
  },

  methods: {
    async getReview() {
      let review = await axios.get("feedback/");
      this.review = review.data;
      for (var i = 0; i < this.review.length; i++) {
        this.review[i].date_created = new Date(this.review[i].date_created);
      }
    }
  }
};
</script>
