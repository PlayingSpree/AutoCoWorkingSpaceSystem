<template>
  <div id="login">
    <v-content>
      <v-card width="350" class="mx-auto" elevation="1">
        <v-card-text class="mt-5">
          <h2 align="center" class="mb-7">Log In to AdminWebsite</h2>
          <v-form>
            <v-text-field
              label="Username"
              name="Username"
              prepend-icon="mdi-account-circle"
              type="text"
              color="blue accent-2"
            >
            </v-text-field>
          </v-form>
          <v-form>
            <v-text-field
              label="Password"
              name="Password"
              prepend-icon="mdi-lock"
              :append-icon="showPassword ? 'mdi-eye' : 'mdi-eye-off'"
              @click:append="showPassword = !showPassword"
              :type="showPassword ? 'text' : 'password'"
              color="blue accent-2"
            >
            </v-text-field>
          </v-form>
          <v-card-actions>
            <v-btn class="mt-7" color="success" block outlined>Log in</v-btn>
          </v-card-actions>
        </v-card-text>
      </v-card>
    </v-content>
  </div>
</template>

<script>
export default {
  name: "login",

  data: () => ({
    step: 1,
    showPassword: false
  }),
  props: {
    source: String
  }
};
</script>

<style></style>
