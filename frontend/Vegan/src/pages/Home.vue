<template>
  <q-page class="row relative-position">
    <!-- <div
      class="absolute row"
      style="min-height: 8vh; top:20px; left: 10px; z-index: 100; width: 100%;"
    >
      <p>ss</p>
      <p>ss2</p>
    </div> -->
    <div class="absolute row top-container">
      <div class="col-12">
        <SearchBar />
      </div>
    </div>

    <div id="map" class="row"></div>
    <div class="absolute row top-container">
      <div class="col-12">
        <RestaurantModal />
      </div>
    </div>
  </q-page>
</template>

<script lang="ts">
import { defineComponent, onMounted, reactive, ref } from "@vue/composition-api";
import { useGMaps, getMap, setMap } from "../modules/useGMaps";
import SearchBar from "components/SearchBar.vue";
import RestaurantModal from "components/RestaurantModal.vue";
import {
  restaurantMapInterface,
  useRestaurant
} from "../modules/useRestaurant";
import { sendNotification } from "../modules/notify";

export default defineComponent({
  name: "HomePage",
  components: { SearchBar, RestaurantModal },
  setup() {
    onMounted(async () => {
      try {
        const {
          initMap,
          placeMarker,
          markerClusterer,
          customMarkers,
          loaded,
          loadMarkers,
          markerFunction,
          markers
        } = await useGMaps();

        if (!loaded.value) {
          setMap(
            await initMap({
              containerID: "map",
              zoom: 13,
              position: { lat: 44.4304, lng: 26.0979 }
            })
          );
          const { ok, error, data } = await loadMarkers();

          if (ok) {
            data.forEach((restaurant: restaurantMapInterface) => {
              customMarkers.value.push({
                marker: placeMarker({
                  position: {
                    lat: Number(restaurant.contact.coordinates.latitude),
                    lng: Number(restaurant.contact.coordinates.longitude)
                  },
                  map: getMap()
                }),
                id: restaurant.id
              });
              markers.value.push(
                placeMarker({
                  position: {
                    lat: Number(restaurant.contact.coordinates.latitude),
                    lng: Number(restaurant.contact.coordinates.longitude)
                  },
                  map: getMap()
                })
              );
            });
          } else {
            sendNotification({
              type: "negative",
              message: "Something went wrong. Please try again"
            });
          }
          markers.value.forEach((marker, index) => {
            markerFunction(marker, index);
          });
          markerClusterer({ map: getMap(), markers: markers.value });
        }
      } catch (error) {
        console.error(error);
      }
    });
    const { restaurants } = useRestaurant();

    return {};
  }
});
</script>

<style lang="scss" scoped>
#map {
  width: 100vw;
  height: inherit;
}

.top-container {
  width: 80%;
  margin-top: 2em;
  left: 10%;
  z-index: 100;
  min-height: 60px;
}
</style>
