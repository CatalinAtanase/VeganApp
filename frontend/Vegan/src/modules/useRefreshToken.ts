import { addMinutes, setExpiresAt } from "./useAccessToken";
import { setAccessToken } from "src/modules/useAccessToken";
import { Cookies } from "quasar";
import { useApi } from "./useApi";
import { setStaticUser } from "./useStaticUser";

export const setRefreshToken = (refresh_token: string) => {
  Cookies.set("refresh_token", refresh_token, {
    expires: "7d"
  });
};

export const deleteRefreshToken = () => {
  Cookies.remove("refresh_token");
};

export const getAccessTokenFromRT = async () => {
  let { apiResponse } = await useApi({
    url: "auth/refresh_token/",
    method: "POST",
    publicRoute: true
  });

  if (!apiResponse.ok) {
    deleteRefreshToken();
    setAccessToken("");

    return false;
  } else {
    setAccessToken(apiResponse.data.access_token);
    setExpiresAt(addMinutes(apiResponse.data.access_token_lifetime));
    setStaticUser(apiResponse.data.user);

    if (apiResponse.data.refresh_token) {
      setRefreshToken(apiResponse.data.refresh_token);
    }

    return true;
  }
};
