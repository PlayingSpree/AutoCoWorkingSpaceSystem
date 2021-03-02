<template>
  <v-card class="mt-5">
    <v-card-title>
      ลำดับความรุนแรงของปัญหา
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
    <v-data-table :headers="headers" :items="reportData" :search="search">
      <template v-slot:item.fixed="{ item }">
        <v-checkbox @click="fixedItem(item)"></v-checkbox>
      </template>
    </v-data-table>
  </v-card>
</template>

<script>
export default {
  data: function() {
    return {
      search: "",
      editedIndex: -1,
      editedItem: {
        name: "",
        comment: "",
        dateandtime: "",
        critical: ""
      },
      headers: [
        {
          text: "รหัส",
          align: "start",
          filterable: true,
          value: "name"
        },
        { text: "รายละเอียด", value: "comment" },
        { text: "วันและเวลา", value: "dateandtime" },
        { text: "ความรุนแรง", value: "critical" },
        { text: "การแก้ไข", value: "fixed", sortable: false }
      ],

      reportData: []
    };
  },
  created() {
    this.initialize();
  },
  methods: {
    initialize: function() {
      this.reportData = [
        {
          name: "001",
          comment: "เปิดประตูไม่ได้",
          dateandtime: "2020-02-8 15:30",
          critical: "รุนแรงมาก"
        },
        {
          name: "002",
          comment: "เปิดแอร์ไม่ได้",
          dateandtime: "2020-02-8 15:30",
          critical: "รุนแรงมาก"
        }
      ];
    },

    fixedItem: function(item) {
      this.editedIndex = this.reportData.indexOf(item);
      this.editedItem = Object.assign({}, item);
      Object.assign(this.reportData[this.editedIndex], this.editedItem)
    }
  }
};
</script>
