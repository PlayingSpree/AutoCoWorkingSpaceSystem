<template>
  <v-card class="mt-5">
    <v-container fluid>
      <v-card-title class="font-size: 20px">
        การรายงานปัญหา
      </v-card-title>
      <v-container class="d-flex align-content-start flex-wrap">
        <v-card width="150px" height="150px" class="mr-2 mb-2" outlined>
          <v-card-title>
            ปัญหา
          </v-card-title>
          <v-card-text>
            {{ appReport() + itemReport() }}
          </v-card-text>
        </v-card>
        <v-card width="150px" height="150px" class="mr-2 mb-2" outlined>
          <v-card-title>
            แอพพลิเคชั่น
          </v-card-title>
          <v-card-text>
            {{ appReport() }}
          </v-card-text>
        </v-card>
        <v-card width="150px" height="150px" class="mr-2 mb-2" outlined>
          <v-card-title>
            อุปกรณ์
          </v-card-title>
          <v-card-text>
            {{ itemReport() }}
          </v-card-text>
        </v-card>
      </v-container>
      <line-chart :data="reportData" />
    </v-container>
  </v-card>
</template>

<script>
export default {
  data: function() {
    return {
      reportData: [
        {
          name: "แอพพลิเคชั่น",
          data: {
            "2020-02-8": 3,
            "2020-02-9": 2,
            "2020-02-10": 1,
            "2020-02-11": 3
          }
        },
        {
          name: "อุปกรณ์",
          data: {
            "2020-02-8": 1,
            "2020-02-9": 2,
            "2020-02-10": 1,
            "2020-02-11": 1
          }
        }
      ]
    };
  },

  methods: {
    appReport: function() {
      return Object.values(this.reportData[0].data).reduce((a, b) => a + b, 0);
    },

    itemReport: function() {
      return Object.values(this.reportData[1].data).reduce((a, b) => a + b, 0);
    }
  }
};
</script>
