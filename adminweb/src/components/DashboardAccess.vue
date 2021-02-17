<template>
  <v-card class="mt-5">
    {{ setAllUser() }}
    <v-container fluid>
      <v-card-title style="font-size:20px">
        การเข้าใช้งาน
      </v-card-title>
      <v-container fluid>
        <v-row>
          <v-col cols="4">
            <v-card outlined style="border-color:#5E35B1">
              <v-card-title style="font-size:1em">
                การเข้าใช้ทั้งหมด
              </v-card-title>
              <v-card-text> {{ allUse() }} </v-card-text>
            </v-card>
          </v-col>
          <v-col cols="4">
            <v-card outlined style="border-color:#303F9F">
              <v-card-title style="font-size:1em">
                Co-working space
              </v-card-title>
              <v-card-text> {{ cowUse() }} </v-card-text>
            </v-card>
          </v-col>
          <v-col cols="4">
            <v-card outlined style="border-color:#FFA726">
              <v-card-title style="font-size:1em">
                Meeting room
              </v-card-title>
              <v-card-text> {{ meetingUse() }} </v-card-text>
            </v-card>
          </v-col>
        </v-row>
        <v-row>
          <v-col cols="12"
            ><v-card outlined>
              <line-chart
                :data="chartData"
                :colors="['#5E35B1', '#303F9F', '#FFA726']"
              ></line-chart> </v-card
          ></v-col>
        </v-row>
      </v-container>
    </v-container>
  </v-card>
</template>

<script>
export default {
  components: {},
  data: function() {
    return {
      chartData: [
        {
          name: "การเข้าใช้งานทั้งหมด",
          data: {
            "2020-02-8": 0,
            "2020-02-9": 0,
            "2020-02-10": 0,
            "2020-02-11": 0,
            "2020-02-12": 0,
            "2020-02-13": 0,
            "2020-02-14": 0
          }
        },
        {
          name: "ยอดขายแพ็คเกจ",
          data: {
            "2020-02-8": 15,
            "2020-02-9": 14,
            "2020-02-10": 17,
            "2020-02-11": 21,
            "2020-02-12": 56,
            "2020-02-13": 67,
            "2020-02-14": 79
          }
        },
        {
          name: "ยอดจองห้องประชุม",
          data: {
            "2020-02-8": 14,
            "2020-02-9": 11,
            "2020-02-10": 7,
            "2020-02-11": 5,
            "2020-02-12": 21,
            "2020-02-13": 22,
            "2020-02-14": 19
          }
        }
      ]
    };
  },

  methods: {
    cowUse: function() {
      var sum = 0;
      for (var key in this.chartData[1].data) {
        sum += this.chartData[1].data[key];
      }
      return sum;
    },

    meetingUse: function() {
      var sum = 0;
      for (var key in this.chartData[2].data) {
        sum += this.chartData[2].data[key];
      }
      return sum;
    },

    allUse: function() {
      return this.cowUse() + this.meetingUse();
    },

    setAllUser: function() {
      for (var key in this.chartData[0].data) {
        this.chartData[0].data[key] =
          this.chartData[1].data[key] + this.chartData[2].data[key];
      }
    }
  }
};
</script>
