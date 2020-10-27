<template>
  <q-layout view="lHh Lpr lFf">
    <q-header elevated>
      <q-toolbar>
        <q-btn
          flat
          dense
          round
          icon="menu"
          aria-label="Menu"
          @click="leftDrawerOpen = !leftDrawerOpen"
        />

        <q-toolbar-title>
          Quasar App
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

    <q-page-container>
      <router-view />
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

import { defineComponent, onBeforeMount, ref } from "@vue/composition-api";
import { useUser } from "../modules/useUser";
import { getAccessToken, setAccessToken } from "../modules/useAccessToken";
import { getStaticUser } from "../modules/useStaticUser";
import { deleteRefreshToken } from "../modules/useRefreshToken";
import { sendNotification } from "../modules/notify";

export default defineComponent({
  name: "MainLayout",
  components: { EssentialLink },
  setup(props, { root }) {
    const leftDrawerOpen = ref(false);
    const essentialLinks = ref(linksData);

    const { setUser, user } = useUser();

    onBeforeMount(async () => {
      if (getAccessToken()) {
        setUser(getStaticUser());
      }
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

    return { leftDrawerOpen, essentialLinks, logout, user };
  }
});
</script>
