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

interface gMapState {
  loaded: boolean;
  markers: google.maps.Marker[];
}

const state = reactive<gMapState>({
  loaded: false,
  markers: []
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
  }: placeMarkerInterface) => {
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

  return { initMap, placeMarker, markerClusterer, ...toRefs(state) };
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
