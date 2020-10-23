import { addMinutes, setAccessToken, setExpiresAt } from "./useAccessToken";
import { useApi } from "./useApi";
import { reactive, toRefs } from "@vue/composition-api";
import { deleteRefreshToken, setRefreshToken } from "./useRefreshToken";

interface User {
  firstName: string;
  lastName: string;
  email: string;
  isLoggedIn: boolean;
}

interface UserStateInterface {
  user: User;
  loading: boolean;
}

const state = reactive<UserStateInterface>({
  user: <User>{
    isLoggedIn: false
  },
  loading: true
});

export const useUser = () => {
  const login = async (email: string, password: string) => {
    const response = {
      ok: Boolean(),
      error: Object(),
      data: Object()
    };

    try {
      let { apiResponse } = await useApi({
        url: "auth/login/",
        method: "POST",
        body: {
          email: email,
          password: password
        },
        publicRoute: true
      });

      response.ok = apiResponse.ok;

      if (!apiResponse.ok) {
        response.error = apiResponse.error;
      } else {
        response.data = apiResponse.data;
        setAccessToken(response.data.access_token);
        setExpiresAt(addMinutes(response.data.access_token_lifetime));
        setUser(response.data.user);

        if (response.data.refresh_token) {
          setRefreshToken(response.data.refresh_token);
        }
      }
    } catch (error) {
      console.log("Login err: ", error);
      response.ok = false;
    }
    return response;
  };

  const register = async (username: string, email: string, password: string) => {
    const response = {
      ok: Boolean(),
      error: Object(),
      data: Object()
    };
    try {
      const { apiResponse } = await useApi({
        url: "auth/register/",
        method: "POST",
        body: {
          username,
          email,
          password
        },
        publicRoute: true
      });
      response.ok = apiResponse.ok;
      console.log(apiResponse);
      

      if (!response.ok) {
        response.error = apiResponse.error;
      } else {
        const { ok, error, data } = await login(email, password);
        response.ok = ok;
        response.error = error;
        response.data = data;
      }
    } catch (error) {
      console.log("Sign up err: ", error);
      response.ok = false;
    }
    return response;
  };

  const changePassword = async (
    oldPassword: string,
    newPassword: string,
    newPassword2: string
  ) => {
    const response = {
      ok: Boolean(),
      error: Object(),
      data: Object()
    };
    try {
      const { apiResponse } = await useApi({
        url: "auth/password_change/",
        method: "PATCH",
        body: {
          old_password: oldPassword,
          new_password1: newPassword,
          new_password2: newPassword2
        }
      });

      response.ok = apiResponse.ok;

      if (!response.ok) {
        response.error = apiResponse.error;
      } else {
        response.data = apiResponse.data;
      }
    } catch (error) {
      console.log("Change password err: ", error);
      response.ok = false;
    }
    return response;
  };

  const resetPassword = async (email: string) => {
    const response = {
      ok: Boolean(),
      error: Object(),
      data: Object()
    };
    try {
      const { apiResponse } = await useApi({
        url: "auth/password_reset/",
        method: "POST",
        body: {
          email
        },
        publicRoute: true
      });

      response.ok = apiResponse.ok;

      if (!response.ok) {
        response.error = apiResponse.error;
      } else {
        response.data = apiResponse.data;
      }
    } catch (error) {
      console.log("Reset password err: ", error);
      response.ok = false;
    }
    return response;
  };

  const resetPasswordConfirm = async (password: string, token: string) => {
    const response = {
      ok: Boolean(),
      error: Object(),
      data: Object()
    };
    try {
      const { apiResponse } = await useApi({
        url: "auth/password_reset/confirm/",
        method: "POST",
        body: {
          password,
          token
        },
        publicRoute: true
      });

      response.ok = apiResponse.ok;

      if (!response.ok) {
        response.error = apiResponse.error;
      } else {
        response.data = apiResponse.data;
      }
    } catch (error) {
      console.log("Reset password Confirm err: ", error);
      response.ok = false;
    }
    return response;
  };

  const setUser = (user: any) => {
    state.user.email = user.email;
    state.user.firstName = user.firstName;
    state.user.lastName = user.lastName;
    state.user.isLoggedIn = true;
  };

  return { login, setUser, ...toRefs(state), register, changePassword, resetPassword, resetPasswordConfirm };
};
