<template>
  <v-card class="mt-5">
    <v-card-title>
      รายละเอียดการรายงานปัญหาของลูกค้า
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
    <v-data-table :headers="headers" :items="report" :search="search">
      <template v-slot:[`item.sev`]="{ item }">
        <v-select v-model="item.sev" @change="setsev(item)" :items="sevlevel" />
      </template>
      <template v-slot:[`item.type`]="{ item }">
        <v-chip :color="getColor(item.type)" style="color: black">
          {{ item.type }}
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
    datatowatch: [],
    all: null
  },
  data: function() {
    return {
      menu: false,
      sevlevel: [
        "แก้ไขเรียบร้อย",
        "ไม่กระทบต่อระบบ",
        "กระทบต่อระบบน้อย",
        "รุนแรง",
        "รุนแรงมาก",
        "รุนแรงมากที่สุด"
      ],
      search: "",
      editedIndex: -1,
      editedItem: {
        id: "",
        text: "",
        type: "",
        date_modified: "",
        severity: null,
        sev: "ยังไม่กำหนด"
      },
      headers: [
        {
          text: "รหัส",
          align: "start",
          filterable: true,
          value: "id"
        },
        { text: "รายละเอียด", value: "text" },
        { text: "ประเภท", value: "type"},
        { text: "วันและเวลา", value: "date_created", width: "30%" },
        { text: "ความรุนแรง", value: "sev", width: "20%" }
      ],

      report: []
    };
  },

  created() {
    this.getReport();
  },

  watch: {
    range(val) {
      this.range[0] = val[0];
      this.range[1] = val[1];
      this.getReport();
    },

    datatowatch: {
      deep: true,
      handler() {
        this.getReport();
      }
    }
  },

  methods: {
    async getReport() {
      let ensev = [];
      for (let i in this.datatowatch) {
        if (this.datatowatch[i] == true) {
          ensev.push(i);
        }
      }
      let report = await axios.get(
        `feedback/problem/?start=${this.range[0]
          .toISOString()
          .substr(0, 10)}&end=${this.range[1].toISOString().substr(0, 10)}`
      );
      report = report.data;
      let enreport = [];
      for (let i = 0; i < report.length; i++) {
        for (let j = 0; j < ensev.length; j++) {
          if (ensev[j] == "null") {
            ensev[j] = null;
          }
          if (report[i].severity == ensev[j]) {
            if (report[i].severity == null) {
              report[i].sev = "";
            } else {
              report[i].sev = this.sevlevel[report[i].severity];
            }
            report[i].date_created = new Date(report[i].date_created);
            report[i].type = report[i].type.name
            enreport.push(report[i]);
            break;
          }
        }
      }
      this.report = enreport;
    },

    async setsev(item) {
      this.editedIndex = this.report.indexOf(item);
      item.severity = this.sevlevel.indexOf(item.sev);
      if (item.severity < 0) {
        item.severity = null;
      }
      this.editedItem = Object.assign({}, item);
      await axios.put(
        `feedback/problem/${this.editedItem.id}/`,
        this.editedItem
      );
      this.getReport();
    },

    getColor(type) {
      if (type == "แอพพลิเคชั่น") return "#C62828";
      else if (type == "อุปกรณ์") return "#FFA726";
    }
  }
};
</script>

<style>
.row-pointer {
  cursor: pointer;
}
</style>
