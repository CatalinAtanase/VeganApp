<template>
  <!-- <q-page class="row items-center justify-evenly"> -->
  <q-page class="row relative-position">
    <!-- <div
      class="absolute row"
      style="min-height: 8vh; top:20px; left: 10px; z-index: 100; width: 100%;"
    >
      <p>ss</p>
      <p>ss2</p>
    </div> -->
    <div id="map" class="row"></div>
  </q-page>
</template>

<script lang="ts">
import { defineComponent, onMounted, ref } from "@vue/composition-api";
import { useGMaps, getMap, setMap } from "../modules/useGMaps";

export default defineComponent({
  name: "PageIndex",
  setup() {
    onMounted(async () => {
      try {
        const {
          initMap,
          placeMarker,
          markerClusterer,
          markers,
          loaded
        } = await useGMaps();

        if (!loaded.value) {
          setMap(
            await initMap({
              containerID: "map",
              zoom: 13,
              position: { lat: 44.4304, lng: 26.0979 }
            })
          );
          markers.value.push(
            placeMarker({
              position: {
                lat: 44.4268,
                lng: 26.1025
              },
              map: getMap()
            })
          );
          markers.value.push(
            placeMarker({
              position: {
                lat: 44.438,
                lng: 26.1025
              },
              map: getMap()
            })
          );
          markerClusterer({ map: getMap(), markers: markers.value });
        }
      } catch (error) {
        console.error(error);
      }
    });
    return {};
  }
});
</script>

<style lang="scss" scoped>
#map {
  width: 100vw;
  height: inherit;
}
</style>
