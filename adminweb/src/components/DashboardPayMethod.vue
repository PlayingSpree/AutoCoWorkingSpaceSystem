<template>
  <v-card class="mt-5">
    <v-card-title style="font-size:20px">
      ช่องทางการชำระเงิน
    </v-card-title>
    <v-container fluid>
      <v-row>
        <v-column>
          <v-card class="mx-4 my-6">
            <v-row>
              <v-column
                ><pie-chart
                  :colors="['#097415', '#1851b2']"
                  :data="pieData"
                  :legend="false"
                  class="pa-3"
                ></pie-chart
              ></v-column>
            </v-row>
          </v-card>
        </v-column>
      </v-row>
    </v-container>
  </v-card>
</template>

<script>
export default {
  data: function() {
    return {
      pieData: [
        ["ชำระผ่านบัตรเครดิต", 770],
        ["ชำระผ่านพร้อมเพย์", 230]
      ]
    };
  }
};
</script>
