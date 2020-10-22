<template>
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
        welcome <br />
        back!
      </p>
    </div>
    <div class="form-container">
      <q-form @submit="onSubmit" @reset="onReset">
        <q-input
          v-model="state.email"
          autofocus
          label="Email"
          color="grey-2"
          label-color="grey-2"
          class="q-my-sm"
          type="email"
          input-style=" color: #fff; font-size: 13px;"
        />
        <q-input
          v-model="state.password"
          label="Password"
          color="grey-2"
          label-color="grey-2"
          class="q-my-sm"
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
        <a href="" class="link text-grey-2">
          Forgot password?
        </a>
        <div class="cta row justify-center q-my-lg">
          <q-btn
            type="submit"
            unelevated
            rounded
            style="background: #40916C;"
            label="Log In"
            class="col-8 text-white q-my-xs btn-font-size text-bold"
            no-caps
          />
        </div>
      </q-form>
    </div>

    <div class="cta row justify-center fixed-bottom q-mb-lg social-container">
      <div class="col-9 separator-container text-center q-mb-md">
        <p><span>or</span></p>
      </div>
      <q-btn
        unelevated
        rounded
        style="background: #7BCE83;"
        label="Log In with Facebook"
        class="col-8 text-white q-my-xs q-py-sm btn-font-size text-bold"
        no-caps
      />
      <q-btn
        unelevated
        rounded
        style="background: #7BCE83;"
        label="Log In with Google"
        class="col-8 text-white q-my-sm q-py-sm btn-font-size text-bold"
        no-caps
      />
    </div>
  </q-page>
</template>

<script lang="ts">
import { defineComponent, reactive, ref } from "@vue/composition-api";

export default defineComponent({
  name: "GetStarted",
  setup(props, {root}) {
    const state = reactive({
      email: "",
      password: "",
      isPwd: true
    });

    const goBack = () => {
      root.$router.push('get_started')
    }

    return { state, goBack };
  }


});
</script>

<style lang="scss" scoped>
.auth-page {
  background: #2d6a4f;
}

.header {
  margin-top: 80px;
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
    margin-top: 30px;
  }

  .social-container {
    margin-bottom: 2.5em;
  }
}

@media screen and (min-height: 730px) {
  .header {
    margin-top: 160px;
  }

  .social-container {
    margin-bottom: 2.5em;
  }
}
</style>
