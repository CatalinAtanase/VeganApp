<template>
  <q-layout view="lHh Lpr lFf">
    <q-header elevated>
      <q-toolbar>
        <!-- <q-btn
          flat
          dense
          round
          icon="menu"
          aria-label="Menu"
          @click="leftDrawerOpen = !leftDrawerOpen"
        /> -->

        <q-toolbar-title>
          VeganApp
        </q-toolbar-title>

        <div>
          Quasar v{{ $q.version }}
          <q-btn
            v-if="user.isLoggedIn"
            flat
            rounded
            color="white"
            label="Logout"
            @click="logout()"
          />
        </div>
      </q-toolbar>
    </q-header>

    <q-drawer
      v-model="leftDrawerOpen"
      show-if-above
      bordered
      content-class="bg-grey-1"
    >
      <q-list>
        <q-item-label header class="text-grey-8">
          Essential Links
        </q-item-label>
        <EssentialLink
          v-for="link in essentialLinks"
          :key="link.title"
          v-bind="link"
        />
      </q-list>
    </q-drawer>

    <q-footer elevated>
      <q-tabs
        no-caps
        v-model="tab"
        indicator-color="transparent"
        active-color="black"
        class="text-grey-9 shadow-2 tabs-container"
        align="justify"
      >
        <q-route-tab
          v-for="(route, index) in routes"
          exact
          :key="index"
          :to="route.to"
          :icon="route.name == $route.name ? route.iconSelected : route.icon"
          :name="route.label"
        />
      </q-tabs>
    </q-footer>

    <q-page-container>
      <keep-alive>
        <router-view />
      </keep-alive>
    </q-page-container>
  </q-layout>
</template>

<script lang="ts">
import EssentialLink from "components/EssentialLink.vue";

const linksData = [
  {
    title: "Docs",
    caption: "quasar.dev",
    icon: "school",
    link: "https://quasar.dev"
  },
  {
    title: "Github",
    caption: "github.com/quasarframework",
    icon: "code",
    link: "https://github.com/quasarframework"
  },
  {
    title: "Discord Chat Channel",
    caption: "chat.quasar.dev",
    icon: "chat",
    link: "https://chat.quasar.dev"
  },
  {
    title: "Forum",
    caption: "forum.quasar.dev",
    icon: "record_voice_over",
    link: "https://forum.quasar.dev"
  },
  {
    title: "Twitter",
    caption: "@quasarframework",
    icon: "rss_feed",
    link: "https://twitter.quasar.dev"
  },
  {
    title: "Facebook",
    caption: "@QuasarFramework",
    icon: "public",
    link: "https://facebook.quasar.dev"
  },
  {
    title: "Quasar Awesome",
    caption: "Community Quasar projects",
    icon: "favorite",
    link: "https://awesome.quasar.dev"
  }
];

const routes = [
  {
    to: { name: "home" },
    name: "home",
    icon: "o_home",
    iconSelected: "home",
    label: "Home"
  },
  {
    to: { name: "index" },
    name: "index",
    icon: "o_explore",
    iconSelected: "explore",
    label: "Explore"
  },
  {
    to: { name: "index" },
    name: "favorites",
    icon: "favorite_border",
    iconSelected: "favorite",
    label: "Favorites"
  },
  {
    to: { name: "profile" },
    name: "profile",
    icon: "o_person",
    iconSelected: "person",
    label: "Profile"
  }
];

import {
  defineComponent,
  onBeforeMount,
  onUnmounted,
  ref
} from "@vue/composition-api";
import { useGMaps } from "../modules/useGMaps";
import { getAccessToken, setAccessToken } from "../modules/useAccessToken";
import { getStaticUser } from "../modules/useStaticUser";
import { useUser } from "../modules/useUser";
import { deleteRefreshToken } from "../modules/useRefreshToken";
import { sendNotification } from "../modules/notify";

export default defineComponent({
  name: "MainLayout",
  components: { EssentialLink },
  setup(props, { root }) {
    const leftDrawerOpen = ref(false);
    const essentialLinks = ref(linksData);
    const tab = ref("");

    const { setUser, user } = useUser();

    onBeforeMount(async () => {
      if (getAccessToken()) {
        setUser(getStaticUser());
      }
    });

    onUnmounted(async () => {
      const { loaded, markers } = await useGMaps();
      markers.value = [];
      loaded.value = false;
    });

    const logout = () => {
      setAccessToken("");
      deleteRefreshToken();
      user.value.isLoggedIn = false;
      sendNotification({
        type: "positive",
        message: "You have been logged out."
      });
      root.$router.push({ name: "login" });
    };

    return { leftDrawerOpen, essentialLinks, routes, tab, logout, user  };
  }
});
</script>

<style lang="scss">
.tabs-container {
  padding-bottom: 12px;
  background: #fafafa;
}

// .q-tab__icon {
//   font-size: 32px;
//   width: 32px;
//   height: 32px;
// }
</style>
