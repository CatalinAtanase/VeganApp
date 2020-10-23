import { Cookies } from "quasar";
import { getAccessToken, getExpiresAt } from "./useAccessToken";
import { getAccessTokenFromRT } from "./useRefreshToken";

const BASE_URL = "http://localhost:8000/api/";

interface apiInterface {
  url: RequestInfo;
  method?: string;
  body?: object;
  publicRoute?: boolean;
}

export const useApi = async ({
  url,
  method = "GET",
  body = {},
  publicRoute = false
}: apiInterface) => {
  const apiResponse = {
    error: "",
    data: Object(),
    ok: Boolean()
  };

  let canDo = true;

  if (!publicRoute) {
    if (getExpiresAt() < new Date()) {
      canDo = await getAccessTokenFromRT();
    }
  }

  if (canDo) {
    let options: RequestInit = {
      method: method,
      headers: {
        "Content-Type": "application/json",
        Authorization: `Token ${getAccessToken()}`,
        "X-CSRFToken": Cookies.get("csrftoken")
      },
      credentials: "include"
    };

    if(method !== 'GET') {
      options.body = JSON.stringify(body)
    }

    try {
      const response = await fetch(`${BASE_URL + url}`, options).catch(err => {
        console.log("fetch: ", err);
      });

      if (response) {
        apiResponse.ok = response.ok
        if (response.ok) {
          apiResponse.data = await response.json();
        } else {
          apiResponse.error = await response.json();
        }
      }
    } catch (error) {
      console.log("fetch err: ", error);
    }
  }

  return { apiResponse };
};
