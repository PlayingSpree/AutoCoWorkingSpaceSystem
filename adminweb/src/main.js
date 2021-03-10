import Vue from "vue";
import App from "./App.vue";
import router from "./router";
import store from "./store";
import vuetify from "./plugins/vuetify";
import Chartkick from "vue-chartkick";
import Chart from "chart.js";
import VueAxios from "vue-axios";
import axios from "axios";

Vue.config.productionTip = false;
Vue.use(Chartkick.use(Chart));

Vue.use(VueAxios, axios);


new Vue({
  router,
  store,
  vuetify,
  render: h => h(App)
}).$mount("#app");
