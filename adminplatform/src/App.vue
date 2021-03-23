<template>
  <v-app>
    <v-app-bar app color="red accent-2" dark>
      <span style="font-size: 40px" class="mx-2">CoSpace</span>
      <v-divider inset vertical></v-divider>
      <span style="font-size: 30px" class="mx-2">User</span>
    </v-app-bar>

    <v-main>
      <v-container fluid class="ma-4">
        <v-row class="d-flex align-center">
          <span class="blue--text text--darken-4  text-h4">Dashboard</span>
          <v-divider></v-divider>
        </v-row>
        <v-container fluid class="mt-5 mx-5">
          <v-row>
            <span>Total server site : {{ site.length }}</span>
          </v-row>
          <v-row class="d-flex align-content-start">
            <v-btn
              class="mx-2"
              :color="
                toshow['Running'] ? 'green darken-2' : 'blue-grey darken-1'
              "
              outlined
              @click="pickshow('Running')"
              >Running: {{ countsitestatus("Running") }}
            </v-btn>
            <v-btn
              class="mx-2"
              :color="
                toshow['Maintaining'] ? 'red accent-4' : 'blue-grey darken-1'
              "
              outlined
              @click="pickshow('Maintaining')"
              >Maintaining: {{ countsitestatus("Maintaining") }}
            </v-btn>
            <v-btn
              class="mx-2"
              :color="
                toshow['Closed'] ? 'pink lighten-3' : 'blue-grey darken-1'
              "
              outlined
              @click="pickshow('Closed')"
              >Closed: {{ countsitestatus("Closed") }}</v-btn
            >
            <v-btn
              class="mx-2"
              :color="
                toshow['Error'] ? 'orange lighten-1' : 'blue-grey darken-1'
              "
              outlined
              @click="pickshow('Error')"
              >Error: {{ countsitestatus("Error") }}
            </v-btn>
          </v-row>
          <v-row class="d-flex align-content-start">
            <v-card
              v-for="item in site"
              :key="item.name"
              class="ma-2"
              width="250px"
              outlined
              :style="borderColor(item.status)"
            >
              <v-card-title class="justify-center">
                {{ item.name }}
              </v-card-title>
              <v-card-text style="font-size:18px">
                <span>Status : {{ item.status }}</span>
              </v-card-text>
              <v-card-actions>
                <v-btn
                  block
                  color="amber darken-1"
                  @click="item.is_active = !item.is_active"
                  >{{ item.is_active ? "pause" : "run"
                  }}<v-icon>{{
                    item.is_active ? "mdi-pause" : "mdi-play"
                  }}</v-icon></v-btn
                >
              </v-card-actions>
            </v-card>
          </v-row>
        </v-container>
      </v-container>
    </v-main>
  </v-app>
</template>

<script>
export default {
  name: "App",

  components: {},

  data: () => ({
    status: ["Running", "Maintaining", "Closed", "Error"],
    site: [],
    countr: 0,
    countm: 0,
    countc: 0,
    counte: 0,
    toshow: { Running: true, Maintaining: true, Closed: true, Error: true }
  }),

  created() {
    this.init();
  },

  watch: {
    toshow: {
      deep: true,
      handler() {
        this.init();
      }
    }
  },

  methods: {
    init() {
      this.site = [];
      this.countr = 0;
      this.countm = 0;
      this.countc = 0;
      this.counte = 0;
      let site = [
        {
          name: "Muffins space",
          status: "Running",
          is_active: true
        },
        {
          name: "space 2",
          status: "Closed",
          is_active: true
        },
        {
          name: "space 3",
          status: "Maintaining",
          is_active: true
        },
        {
          name: "space 4",
          status: "Error",
          is_active: true
        },
        {
          name: "space 5",
          status: "Running",
          is_active: true
        },
        {
          name: "space 6",
          status: "Running",
          is_active: true
        }
      ];

      let toshow = [];
      for (let i in this.toshow) {
        if (this.toshow[i] == true) {
          toshow.push(i);
        }
      }

      for (let i = 0; i < site.length; i++) {
        if (toshow.includes(site[i].status)) {
          this.site.push(site[i]);
        }
      }

      for (let i = 0; i < this.site.length; i++) {
        if (this.site[i].status == "Running") {
          this.countr += 1;
        } else if (this.site[i].status == "Maintaining") {
          this.countm += 1;
        } else if (this.site[i].status == "Closed") {
          this.countc += 1;
        } else {
          this.counte += 1;
        }
      }
    },
    borderColor(status) {
      if (status == "Running") return "border-color: #388E3C";
      else if (status == "Maintaining") return "border-color: #D50000";
      else if (status == "Closed") return "border-color: #F48FB1";
      else return "border-color: #FFA726";
    },
    countsitestatus(status) {
      if (status == "Running") return this.countr;
      else if (status == "Maintaining") return this.countm;
      else if (status == "Closed") return this.countc;
      else return this.counte;
    },
    pickshow(status) {
      this.toshow[status] = !this.toshow[status];
    }
  }
};
</script>
