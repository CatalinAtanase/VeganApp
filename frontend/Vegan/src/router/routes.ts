import { RouteConfig } from "vue-router";

const routes: RouteConfig[] = [
  {
    path: "/",
    component: () => import("layouts/MainLayout.vue"),
    children: [
      { path: "", component: () => import("pages/Home.vue"), name: "home" },
      { path: "index", component: () => import("pages/Index.vue"), name: "index" }
    ]
  },
  {
    path: "/",
    component: () => import("layouts/AuthLayout.vue"),
    children: [
      { path: "get_started", component: () => import("pages/GetStarted.vue"), name: "getStarted" },
      { path: "login", component: () => import("pages/auth/Login.vue"), name: "login" },
      { path: "register", component: () => import("pages/auth/Register.vue"), name: "register" },
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
