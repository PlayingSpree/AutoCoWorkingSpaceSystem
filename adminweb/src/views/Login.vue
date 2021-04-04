<template>
  <div id="login">
    <v-content>
      <v-card width="350" class="mx-auto" elevation="1" outlined>
        <v-card-text class="mt-5">
          <h2 align="center" class="mb-7">Log In to AdminWebsite</h2>
          <v-form @submit.prevent="submit">
            <v-text-field
              label="Username"
              v-model="form.email"
              name="Username"
              prepend-icon="mdi-account-circle"
              type="text"
              color="blue accent-2"
            >
            </v-text-field>
            <v-text-field
              label="Password"
              name="Password"
              v-model="form.password"
              prepend-icon="mdi-lock"
              :append-icon="showPassword ? 'mdi-eye' : 'mdi-eye-off'"
              @click:append="showPassword = !showPassword"
              :type="showPassword ? 'text' : 'password'"
              color="blue accent-2"
            >
            </v-text-field>
            <v-btn class="mt-7" color="success" block outlined type="submit"
              >Log in</v-btn
            >
          </v-form>
        </v-card-text>
      </v-card>
    </v-content>
  </div>
</template>

<script>
import { mapActions } from "vuex";

export default {
  name: "login",

  data: () => ({
    form: {
      email: "",
      password: ""
    },
    step: 1,
    showPassword: false
  }),

  methods: {
    ...mapActions({
      logIn: "auth/logIn"
    }),

    submit() {
      this.logIn(this.form).then(() => {
        this.$router.push("/dashboard");
      });
    }
  }
};
</script>

<style></style>
