import Vue from "vue";
import VueRouter, { RouteConfig } from "vue-router";

Vue.use(VueRouter);

// route level code-splitting
// this generates a separate chunk (about.[hash].js) for this route
// which is lazy-loaded when the route is visited.
const routes: Array<RouteConfig> = [
  {
    path: "/comm",
    name: "Comm",
    component: () =>
      import("../views/Home.vue")
  },
  {
    path: "/ports",
    name: "Ports",
    component: () =>
      import("../views/Ports.vue")
  },
  {
    path: "/acl",
    name: "ACL",
    component: () =>
      import("../views/ACL.vue")
  },
  {
    path: "/qos",
    name: "QoS",
    component: () =>
      import("../views/QoS.vue")
  }
];

const router = new VueRouter({
  mode: "history",
  base: process.env.BASE_URL,
  routes
});

export default router;
