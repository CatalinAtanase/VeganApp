<template>
  <!-- <div class="" style=""> --> <!-- Add this div for responsive design -->
    <q-page class="column auth-page q-px-xl">
      <q-icon
        name="clear"
        class="cursor-pointer fixed-top-left q-ma-sm q-pa-sm"
        color="grey-2"
        size="sm"
        @click="goBack"
      />
      <div class="header">
        <p class="text-h4 text-white text-bold">
          create an <br />
          account
        </p>
      </div>
      <div class="form-container">
        <q-form @submit="onSubmit">
          <q-input
            v-model="state.username"
            autofocus
            label="Username"
            color="grey-2"
            label-color="grey-2"
            class="q-my-xs"
            input-style=" color: #fff; font-size: 13px;"
          />
          <q-input
            v-model="state.email"
            label="Email"
            color="grey-2"
            label-color="grey-2"
            class="q-my-xs"
            input-style=" color: #fff; font-size: 13px;"
          />
          <q-input
            v-model="state.password"
            label="Password"
            color="grey-2"
            label-color="grey-2"
            class="q-my-xs"
            input-style=" color: #fff; font-size: 13px;"
            :type="state.isPwd ? 'password' : 'text'"
          >
            <template v-slot:append>
              <q-icon
                :name="state.isPwd ? 'visibility_off' : 'visibility'"
                class="cursor-pointer"
                @click="state.isPwd = !state.isPwd"
                color="grey-2"
              />
            </template>
          </q-input>
          <q-input
            v-model="state.password2"
            label="Repeat Passsword"
            color="grey-2"
            label-color="grey-2"
            class="q-my-xs"
            input-style=" color: #fff; font-size: 13px;"
            :type="state.isPwd2 ? 'password' : 'text'"
          >
            <template v-slot:append>
              <q-icon
                :name="state.isPwd2 ? 'visibility_off' : 'visibility'"
                class="cursor-pointer"
                @click="state.isPwd2 = !state.isPwd2"
                color="grey-2"
              />
            </template>
          </q-input>
          <a href="" class="link text-grey-2">
            Forgot password?
          </a>
          <div class="cta row justify-center q-my-lg">
            <q-btn
              type="submit"
              unelevated
              rounded
              style="background: #40916C;"
              label="Sign Up"
              class="col-9 text-white q-my-xs btn-font-size text-bold"
              no-caps
            />
          </div>
        </q-form>
      </div>

      <div class="cta row justify-center q-mb-lg social-container">
        <div class="col-12 separator-container text-center q-mb-md">
          <p><span>or</span></p>
        </div>
        <q-btn
          unelevated
          rounded
          style="background: #7BCE83;"
          label="Log In with Facebook"
          class="col-12 text-white q-my-xs q-py-sm btn-font-size text-bold"
          no-caps
        />
        <q-btn
          unelevated
          rounded
          style="background: #7BCE83;"
          label="Log In with Google"
          class="col-12 text-white q-my-sm q-py-sm btn-font-size text-bold"
          no-caps
        />
      </div>
    </q-page>
  <!-- </div> -->
</template>

<script lang="ts">
import { defineComponent, reactive, ref } from "@vue/composition-api";
import { sendNotification } from "../../modules/notify";
import { useUser } from "../../modules/useUser";

export default defineComponent({
  name: "GetStarted",
  setup(props, { root }) {
    const state = reactive({
      username: "",
      email: "",
      password: "",
      password2: "",
      isPwd: true,
      isPwd2: true,
      accept: false
    });

    const { login, register } = useUser();

    const onSubmit = async () => {
      let errors = [];
      if (state.password != state.password2) {
        errors.push("Passwords don't match");
      }
      // if (!state.accept) {
      //   errors.push("You must accept the terms and conditions");
      // }

      if (errors.length == 0) {
        try {
          const { ok, error, data } = await register(
            state.username,
            state.email,
            state.password
          );

          if (ok) {
            sendNotification({
              type: "positive",
              message: `${
                data.message ? data.message : "Your account has been created."
              }`,
              timeout: 1000
            });

            root.$router.push((root.$route.query.redirect as string) || "/");
          } else {
            for (let key in error) {
              sendNotification({
                type: "negative",
                message: `${error[key]}`,
                timeout: 1000
              });
            }
          }
        } catch (error) {
          console.log("login comp: ", error.response.data);
        }
      } else {
        errors.forEach(err => {
          sendNotification({
            type: "negative",
            message: `${err}`,
            timeout: 2000
          });
        });
      }
    };

    const goBack = () => {
      root.$router.push({ name: "getStarted" });
    };

    return { state, goBack, onSubmit };
  }
});
</script>

<style lang="scss" scoped>
.auth-page {
  background: #2d6a4f;
}

.header {
  margin-top: 25px;
}

.btn-font-size {
  font-size: 1.2em;
  padding: 3px 8px;
}

.link {
  text-decoration: underline;
  opacity: 0.8;
  padding: 3px 6px;
  margin-left: -3px;
  font-size: 13px;
}

.separator-container {
  p {
    width: 100%;
    text-align: center;
    border-bottom: 1px solid #fff;
    line-height: 0.15em;
    margin: 10px 0 0px;
  }

  p span {
    color: #fff;
    background: #2d6a4f;
    padding: 0 18px;
  }
}

@media screen and (max-height: 570px) {
  .header {
    margin-top: 10px;
  }

  .social-container {
    margin-bottom: 2.5em;
  }
}

@media screen and (min-height: 730px) {
  .header {
    margin-top: 80px;
  }

  .social-container {
    margin-bottom: 2.5em;
  }
}
</style>
