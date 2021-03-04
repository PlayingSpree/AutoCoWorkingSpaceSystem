import Vue from "vue";
import VueRouter from "vue-router";
import Login from "../views/Login.vue";
import Dashboard from "../views/Dashboard.vue";
import Manage from "../views/Management.vue";
import Review from "../views/Review.vue";
import Report from "../views/Report.vue";
import User from "../views/User.vue";

Vue.use(VueRouter);

const routes = [
  {
    path: "/",
    name: "Dashboard",
    component: Dashboard
  },
  {
    path: "/login",
    name: "Login",
    component: Login
  },
  {
    path: "/manage",
    name: "Manage",
    component: Manage
  },
  {
    path: "/review",
    name: "Review",
    component: Review
  },
  {
    path: "/report",
    name: "Report",
    component: Report
  },
  {
    path: "/user",
    name: "User",
    component: User
  }
];

const router = new VueRouter({
  mode: "history",
  base: process.env.BASE_URL,
  routes
});

export default router;
