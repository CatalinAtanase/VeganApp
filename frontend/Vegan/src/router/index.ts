import { Cookies } from 'quasar';
import { route } from 'quasar/wrappers';
import { getAccessToken } from 'src/modules/useAccessToken';
import { getAccessTokenFromRT } from 'src/modules/useRefreshToken';
import VueRouter from 'vue-router';
import { Store } from "vuex";
import { StateInterface } from '../store';
import routes from './routes';

/*
 * If not building with SSR mode, you can
 * directly export the Router instantiation
 */

export default route<Store<StateInterface>>(function ({ Vue }) {
  Vue.use(VueRouter);

  const Router = new VueRouter({
    scrollBehavior: () => ({ x: 0, y: 0 }),
    routes,

    // Leave these as is and change from quasar.conf.js instead!
    // quasar.conf.js -> build -> vueRouterMode
    // quasar.conf.js -> build -> publicPath
    mode: process.env.VUE_ROUTER_MODE,
    base: process.env.VUE_ROUTER_BASE
  });

  Router.beforeEach(async (to, from, next) => {
    let hasCredentials = getAccessToken() ? true : false;

    if (!hasCredentials) {
      if (Cookies.get("refresh_token")) {
        hasCredentials = await getAccessTokenFromRT();
      }
    }

    let publicRoutes = ["login", "register", "resetPassword", "resetPasswordConfirm", "getStarted"];

    if (publicRoutes.includes(to.name as string) && hasCredentials) {
      next({ name: "home" });
    } else if (!publicRoutes.includes(to.name as string) && !hasCredentials) {
      next({ name: "login", query: { redirect: to.path } });
    } else next();
  });

  return Router;
})
