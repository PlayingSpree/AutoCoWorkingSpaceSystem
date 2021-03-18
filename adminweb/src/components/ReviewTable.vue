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
      <template v-slot:[`item.rating`]="{ item }">
        <v-chip :color="getColor(item.rating)" style="color: black">
          {{ item.rating }}
        </v-chip>
      </template>
    </v-data-table>
  </v-card>
</template>

<script>
import axios from "axios";

export default {
  props: {
    range: [],
    datatowatch: []
  },
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

  watch: {
    range(val) {
      this.range[0] = val[0];
      this.range[1] = val[1];
      this.getReview();
    },

    datatowatch: {
      deep: true,
      handler() {
        this.getReview();
      }
    }
  },

  methods: {
    async getReview() {
      let enstar = [];

      for (let i in this.datatowatch) {
        if (this.datatowatch[i] == true) {
          enstar.push(i);
        }
      }
      let review = await axios.get(
        `feedback/?start=${this.range[0]
          .toISOString()
          .substr(0, 10)}&end=${this.range[1].toISOString().substr(0, 10)}`
      );
      review = review.data;
      let enreview = [];
      for (let i = 0; i < review.length; i++) {
        for (let j = 0; j < enstar.length; j++) {
          if (review[i].rating == enstar[j]) {
            review[i].date_created = new Date(review[i].date_created);
            enreview.push(review[i]);
          }
        }
      }
      this.review = enreview;
    },

    getColor(rating) {
      if (rating == 1) return "#C62828";
      else if (rating == 2) return "#EF6C00";
      else if (rating == 3) return "#FDD835";
      else if (rating == 4) return "#76FF03";
      else return "#388E3C";
    }
  }
};
</script>
