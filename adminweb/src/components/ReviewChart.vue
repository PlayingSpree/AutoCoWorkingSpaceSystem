<template>
  <v-card class="mt-5">
    <v-container fluid>
      <v-card-title style="font-size: 20px">
        คะแนนความพึงพอใจ
      </v-card-title>
      <v-container class="d-flex align-content-start flex-wrap">
        <v-card width="150px" height="100px" class="mr-2 mb-2" outlined>
          <v-card-title>
            คะแนนเฉลี่ย
          </v-card-title>
          <v-card-text>
            {{ avgScore() }}
          </v-card-text>
        </v-card>
        <v-card width="150px" height="100px" class="mr-2 mb-2" outlined>
          <v-card-title>
            1 ดาว
          </v-card-title>
          <v-card-text>
            {{ countStar()[0] }}
          </v-card-text>
        </v-card>
        <v-card width="150px" height="100px" class="mr-2 mb-2" outlined>
          <v-card-title>
            2 ดาว
          </v-card-title>
          <v-card-text>
            {{ countStar()[1] }}
          </v-card-text>
        </v-card>
        <v-card width="150px" height="100px" class="mr-2 mb-2" outlined>
          <v-card-title>
            3 ดาว
          </v-card-title>
          <v-card-text>
            {{ countStar()[2] }}
          </v-card-text>
        </v-card>
        <v-card width="150px" height="100px" class="mr-2 mb-2" outlined>
          <v-card-title>
            4 ดาว
          </v-card-title>
          <v-card-text>
            {{ countStar()[3] }}
          </v-card-text>
        </v-card>
        <v-card width="150px" height="100px" class="mr-2 mb-2" outlined>
          <v-card-title>
            5 ดาว
          </v-card-title>
          <v-card-text>
            {{ countStar()[4] }}
          </v-card-text>
        </v-card>
      </v-container>
      <line-chart :data="chartData"></line-chart>
    </v-container>
  </v-card>
</template>

<script>
export default {
  data: function() {
    return {
      chartData: [
        {
          name: "1",
          data: {
            "2020-02-8": 0,
            "2020-02-9": 1,
            "2020-02-10": 1,
            "2020-02-11": 1,
            "2020-02-12": 0
          }
        },
        {
          name: "2",
          data: {
            "2020-02-8": 2,
            "2020-02-9": 0,
            "2020-02-10": 1,
            "2020-02-11": 0,
            "2020-02-12": 1
          }
        },
        {
          name: "3",
          data: {
            "2020-02-8": 3,
            "2020-02-9": 0,
            "2020-02-10": 2,
            "2020-02-11": 0,
            "2020-02-12": 0
          }
        },
        {
          name: "4",
          data: {
            "2020-02-8": 3,
            "2020-02-9": 4,
            "2020-02-10": 1,
            "2020-02-11": 2,
            "2020-02-12": 5
          }
        },
        {
          name: "5",
          data: {
            "2020-02-8": 2,
            "2020-02-9": 1,
            "2020-02-10": 3,
            "2020-02-11": 2,
            "2020-02-12": 1
          }
        }
      ]
    };
  },

  methods: {
    avgScore: function() {
      var sum = 0;
      var count = 0;
      for (var i = 0; i < 5; i++) {
        var counti = Object.values(this.chartData[i].data).reduce(
          (a, b) => a + b,
          0
        );
        count += counti;
        sum += counti * (i + 1);
      }
      return (sum / count).toFixed(2);
    },

    countStar: function() {
      var countStar = [];

      for (var i = 0; i < 5; i++) {
        var counti = Object.values(this.chartData[i].data).reduce(
          (a, b) => a + b,
          0
        );
        countStar.push(counti);
      }
      return countStar;
    }
  }
};
</script>
