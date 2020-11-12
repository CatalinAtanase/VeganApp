import { reactive, toRefs } from "@vue/composition-api";
interface contactInterface {
  address: string;
  coordinates: {
    latitude: string;
    longitude: string;
    // Needs to be parsed
  };
  email: string;
  phone_number: string;
  website_url: string;
}

interface imageInterface {
  image: string;
}

interface restaurantBadge {
  color: string;
  icon: {
    icon: string;
    name: string;
    description: string;
  };
}

export interface restaurantMapInterface {
  id: number;
  contact: contactInterface;
  images: Array<imageInterface>;
  name: string;
  badge: restaurantBadge[];
}

export interface restaurantsState {
  restaurants: restaurantMapInterface[];
}

const state = reactive<restaurantsState>({
  restaurants: []
});

export const useRestaurant = () => {
  return { ...toRefs(state) };
};
