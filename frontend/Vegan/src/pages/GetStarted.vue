<template>
  <q-page class="column items-center auth-page ">
    <div class="logo" style="margin-top: 180px;">
      <q-icon name="nature" class="text-teal" style="font-size: 8em;" />
      <p class="text-h5 text-white text-bold">Vegan App</p>
    </div>
    <div class="cta row justify-center fixed-bottom q-mb-xl">
      <q-btn
        unelevated
        rounded
        style="background: #7BCE83;"
        label="Get Started"
        class="col-9 text-white q-my-xs q-py-sm btn-font-size text-bold"
        to="/register"
        no-caps
      />
      <q-btn
        unelevated
        rounded
        style="background: #D3D3D3;"
        label="Log In"
        class="col-9 text-white q-my-sm q-py-sm btn-font-size text-bold"
        to="/login"
        no-caps
      />
    </div>
  </q-page>
</template>

<script lang="ts">
import { defineComponent, ref } from "@vue/composition-api";

export default defineComponent({
  name: "GetStarted",
  setup() {
    return {};
  }
});
</script>

<style lang="scss" scoped>
.auth-page {
  background: #2d6a4f;
}

.btn-font-size {
  font-size: 1.2em;
  // font-size: 22px;
}
</style>
