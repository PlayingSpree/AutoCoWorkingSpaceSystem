<template>
  <v-card class="mt-5">
    <v-card-actions>
      <p class="my-auto mx-2">กรองข้อมูลความรุนแรง</p>
      <v-btn @click="emitall" outlined :color="all ? 'red' : 'red lighten-4'"
        >ทั้งหมด</v-btn
      >
      <v-btn
        @click="emitstate('null')"
        outlined
        :color="datatowatch['null'] ? 'white' : 'grey darken-2'"
        >ยังไม่กำหนด</v-btn
      >
      <v-btn
        @click="emitstate(0)"
        outlined
        :color="datatowatch[0] ? 'white' : 'grey darken-2'"
        >แก้ไขเรียบร้อย</v-btn
      >
      <v-btn
        @click="emitstate(1)"
        outlined
        :color="datatowatch[1] ? 'white' : 'grey darken-2'"
        >ไม่กระทบต่อระบบ</v-btn
      >
      <v-btn
        @click="emitstate(2)"
        outlined
        :color="datatowatch[2] ? 'white' : 'grey darken-2'"
        >กระทบต่อระบบน้อย</v-btn
      >
      <v-btn
        @click="emitstate(3)"
        outlined
        :color="datatowatch[3] ? 'white' : 'grey darken-2'"
        >รุนแรง</v-btn
      >
      <v-btn
        @click="emitstate(4)"
        outlined
        :color="datatowatch[4] ? 'white' : 'grey darken-2'"
        >รุนแรงมาก</v-btn
      >
      <v-btn
        @click="emitstate(5)"
        outlined
        :color="datatowatch[5] ? 'white' : 'grey darken-2'"
        >รุนแรงมากที่สุด</v-btn
      >
    </v-card-actions>
  </v-card>
</template>

<script>
export default {
  props: {
    datatowatch: {},
    all: null
  },
  data: function() {
    return {};
  },
  methods: {
    emitall() {
      this.all = !this.all;

      if (this.all == true) {
        this.datatowatch[1] = true;
        this.datatowatch[2] = true;
        this.datatowatch[3] = true;
        this.datatowatch[4] = true;
        this.datatowatch[5] = true;
        this.datatowatch[0] = true;
        this.datatowatch["null"] = true;
      } else {
        this.datatowatch[1] = false;
        this.datatowatch[2] = false;
        this.datatowatch[3] = false;
        this.datatowatch[4] = false;
        this.datatowatch[5] = false;
        this.datatowatch[0] = false;
        this.datatowatch["null"] = false;
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
        this.datatowatch[5] == false ||
        this.datatowatch[0] == false ||
        this.datatowatch["null"] == false
      ) {
        this.all = false;
      }
      if (
        this.datatowatch[1] == true &&
        this.datatowatch[2] == true &&
        this.datatowatch[3] == true &&
        this.datatowatch[4] == true &&
        this.datatowatch[5] == true &&
        this.datatowatch[0] == true &&
        this.datatowatch["null"] == true
      ) {
        this.all = true;
      }
      this.$emit("getallstate", this.all);
      this.$emit("getnewstate", this.datatowatch);
    }
  }
};
</script>
