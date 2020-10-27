import { RouteConfig } from "vue-router";

const routes: RouteConfig[] = [
  {
    path: "/",
    component: () => import("layouts/MainLayout.vue"),
    children: [{ path: "", component: () => import("pages/Index.vue"), name: "home" }]
  },
  {
    path: "/",
    component: () => import("layouts/AuthLayout.vue"),
    children: [
      { path: "get_started", component: () => import("pages/GetStarted.vue"), name: "getStarted" },
      { path: "login", component: () => import("pages/Login.vue"), name: "login" },
      { path: "register", component: () => import("pages/Register.vue"), name: "register" },
    ]
  },

  // Always leave this as last one,
  // but you can also remove it
  {
    path: "*",
    component: () => import("pages/Error404.vue")
  }
];

export default routes;
