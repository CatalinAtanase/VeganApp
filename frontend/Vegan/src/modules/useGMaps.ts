import { useRestaurant } from './useRestaurant';
import { useApi } from "./useApi";
import { toRefs } from "@vue/composition-api";
import { reactive } from "@vue/composition-api";
import gmapsInit from "../utils/gmap";
import MarkerClusterer from "@google/markerclustererplus";

interface positionInterface {
  lat: number;
  lng: number;
}

interface initMapInterface {
  containerID: string;
  zoom: number;
  position: positionInterface;
}

interface placeMarkerInterface {
  position: positionInterface;
  map: google.maps.Map;
  moveTo?: boolean; // If to change the center of the map to the given position.
}

interface MarkerClustererInterface {
  map: google.maps.Map;
  markers: google.maps.Marker[];
}

interface customMarkersInterface {
  marker: google.maps.Marker,
  id: number
}

interface gMapState {
  loaded: boolean;
  markers: google.maps.Marker[];
  customMarkers: customMarkersInterface[];
}


const state = reactive<gMapState>({
  loaded: false,
  markers: [],
  customMarkers: [],
});

let map: google.maps.Map;
export const getMap = (): google.maps.Map => {
  return map;
};

export const setMap = (gMap: google.maps.Map) => {
  map = gMap;
};

export const useGMaps = async () => {
  const google = await gmapsInit();

  const initMap = ({ containerID, zoom, position }: initMapInterface) => {
    if (!state.loaded) {
      setMap(
        new google.maps.Map(
          document.getElementById(containerID) as HTMLElement,
          {
            zoom,
            center: position,
            fullscreenControl: false,
            gestureHandling: "greedy",
            zoomControl: false
          }
        )
      );
    }

    state.loaded = true;

    return getMap();
  };

  const placeMarker = ({
    position,
    map,
    moveTo = false
  }: placeMarkerInterface): google.maps.Marker => {
    const marker: google.maps.Marker = new google.maps.Marker({
      position,
      map
    });

    if (moveTo) {
      map.panTo(position);
    }

    return marker;
  };

  const markerClusterer = ({ map, markers }: MarkerClustererInterface) => {
    new MarkerClusterer(map, markers, {
      imagePath:
        "https://developers.google.com/maps/documentation/javascript/examples/markerclusterer/m"
    });
  };

  const loadMarkers = async () => {
    const response = {
      ok: Boolean(),
      error: Object(),
      data: Object()
    };
    try {
      const { apiResponse } = await useApi({
        url: "restaurants-map",
      });
      
      if (!apiResponse.ok) {
        response.error = apiResponse.error;
      } else {
        response.data = apiResponse.data;
      }
      response.ok = apiResponse.ok

      // load restaurants
      const {restaurants} = useRestaurant()
      restaurants.value = response.data

      return response
    } catch (error) {
      console.log(error);
      return error
    }
  };

  const markerFunction = (marker: google.maps.Marker, index: number) => {
    marker.addListener("click", () => {
      // @ts-ignore
      getMap().panTo(marker.getPosition())
      console.log(state.customMarkers[index].id);
    })
  }

  return { initMap, placeMarker, markerClusterer, ...toRefs(state), loadMarkers, markerFunction };
};

/* MAP PROPERTIES

backgroundColor
center
clickableIcons
controlSize
disableDefaultUI
disableDoubleClickZoom
draggable
draggableCursor
draggingCursor, 
fullscreenControl, 
fullscreenControlOptions, 
gestureHandling, 
heading, 
keyboardShortcuts, 
mapTypeControl, 
mapTypeControlOptions,
mapTypeId, 
maxZoom, 
minZoom, 
noClear, 
panControl, 
panControlOptions, 
restriction, 
rotateControl, 
rotateControlOptions, 
scaleControl, 
scaleControlOptions, 
scrollwheel, 
streetView, 
streetViewControl, 
streetViewControlOptions, 
styles, 
tilt, 
zoom, 
zoomControl, 
zoomControlOptions

link https://developers.google.com/maps/documentation/javascript/reference/map#MapTypeStyle
*/

/*

LINK for google.maps.Map + events
https://developers.google.com/maps/documentation/javascript/reference

*/

// Link general https://developers.google.com/maps/documentation/javascript/reference

// Click event https://developers.google.com/maps/documentation/javascript/examples/event-simple
