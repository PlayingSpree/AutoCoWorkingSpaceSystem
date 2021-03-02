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
export default {
  data: function() {
    return {
      search: "",
      headers: [
        {
          text: "รหัส",
          align: "start",
          filterable: true,
          value: "name"
        },
        { text: "รายละเอียด", value: "comment" },
        { text: "วันและเวลา", value: "dateandtime" },
        { text: "คะแนน", value: "score" }
      ],
      review: [
        {
          name: "001",
          comment: "ดีมากก",
          dateandtime: new Date("2020-02-8 15:30"),
          score: 5
        },
        {
          name: "002",
          comment: "พอใช้",
          dateandtime: new Date("2020-02-8 16:30"),
          score: 3
        },
        {
          name: "003",
          comment: "ดีมาก",
          dateandtime: new Date("2020-02-9 15:30"),
          score: 4
        },
        {
          name: "004",
          comment: "ดีมากก",
          dateandtime: new Date("2020-02-10 15:30"),
          score: 5
        },
        {
          name: "005",
          comment: "แย่",
          dateandtime: new Date("2020-02-11 15:30"),
          score: 2
        }
      ]
    };
  }
};
</script>
