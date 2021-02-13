<template>
  <v-card class="mt-5">
    <v-card-title style="font-size:20px">
      ภาพรวมผู้ซื้อ
    </v-card-title>
    <v-container fluid>
      <v-row>
        <pie-chart :data="pieData"></pie-chart>
      </v-row>
    </v-container>
  </v-card>
</template>

<script>
export default {
  data: function() {
    return {
      pieData: [
        ["NewUser", 10],
        ["OldUser", 34]
      ]
    };
  }
};
</script>
