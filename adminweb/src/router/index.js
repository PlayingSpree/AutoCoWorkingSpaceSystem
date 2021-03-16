import Vue from "vue";
import VueRouter from "vue-router";
import Login from "../views/Login.vue";
import Dashboard from "../views/Dashboard.vue";
import Manage from "../views/Management.vue";
import Review from "../views/Review.vue";
import Report from "../views/Report.vue";
import User from "../views/User.vue";
import store from "@/store";

Vue.use(VueRouter);

const routes = [
  {
    path: "/",
    redirect: {
      name: "Login"
    }
  },
  {
    path: "/dashboard",
    name: "Dashboard",
    component: Dashboard,
    beforeEnter: (to, from, next) => {
      if (!store.getters["auth/authenicated"]) {
        return next({
          name: "Login"
        });
      } else {
        next();
      }
    }
  },
  {
    path: "/login",
    name: "Login",
    component: Login,
    beforeEnter: (to, from, next) => {
      if (store.getters["auth/authenicated"]) {
        return next({
          name: "Dashboard"
        });
      } else {
        next();
      }
    }
  },
  {
    path: "/manage",
    name: "Manage",
    component: Manage,
    beforeEnter: (to, from, next) => {
      if (!store.getters["auth/authenicated"]) {
        return next({
          name: "Login"
        });
      } else {
        next();
      }
    }
  },
  {
    path: "/review",
    name: "Review",
    component: Review,
    beforeEnter: (to, from, next) => {
      if (!store.getters["auth/authenicated"]) {
        return next({
          name: "Login"
        });
      } else {
        next();
      }
    }
  },
  {
    path: "/report",
    name: "Report",
    component: Report,
    beforeEnter: (to, from, next) => {
      if (!store.getters["auth/authenicated"]) {
        return next({
          name: "Login"
        });
      } else {
        next();
      }
    }
  },
  {
    path: "/user",
    name: "User",
    component: User,
    beforeEnter: (to, from, next) => {
      if (!store.getters["auth/authenicated"]) {
        return next({
          name: "Login"
        });
      } else {
        next();
      }
    }
  }
];

const router = new VueRouter({
  mode: "history",
  base: process.env.BASE_URL,
  routes
});

export default router;
