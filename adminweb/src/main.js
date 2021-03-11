import Vue from "vue";
import App from "./App.vue";
import router from "./router";
import store from "./store";
import vuetify from "./plugins/vuetify";
import Chartkick from "vue-chartkick";
import Chart from "chart.js";
import VueAxios from "vue-axios";
import axios from "axios";

require("@/store/subscriber");

axios.defaults.baseURL = "http://127.0.0.1:8000/";

Vue.config.productionTip = false;
Vue.use(Chartkick.use(Chart));

Vue.use(VueAxios, axios);

store.dispatch("auth/attempt", localStorage.getItem("token")).then(() => {
  new Vue({
    router,
    store,
    vuetify,
    render: h => h(App)
  }).$mount("#app");
});
