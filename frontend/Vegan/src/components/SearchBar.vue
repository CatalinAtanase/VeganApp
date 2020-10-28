<template>
  <div class="search-container">
    <q-input
      placeholder="Caută un restaurant"
      ref="searchInput"
      rounded
      outlined
      v-model="state.searchInput"
      bg-color="white"
      color="black"
      dense
    >
    <!-- label | placehodler -->
      <template v-slot:prepend>
        <q-icon name="place" />
      </template>
      <template v-slot:append>
        <q-icon
          name="search"
          @click="$refs.searchInput.focus()"
          class="cursor-pointer"
        />
      </template>
      <!-- <template v-slot:hint>
      Field hint
    </template> -->
    </q-input>
  </div>
</template>

<script lang="ts">
import { defineComponent, reactive } from "@vue/composition-api";
export default defineComponent({
  name: "searchBar",
  setup(props, { root }) {
    const state = reactive({
      searchInput: ""
    })
    return {state};
  }
});
</script>

<style lang="scss">

</style>
