<template>
  <v-app>
    <v-app-bar app>
      <v-btn @click="$router.push('/')" text>Dashboard</v-btn>
      <v-btn @click="$router.push('/manage')" text>Management</v-btn>
      <v-btn @click="$router.push('/login')" text>Review</v-btn>
      <v-btn @click="$router.push('/login')" text>Report</v-btn>
      <v-btn @click="$router.push('/login')" text>User</v-btn>
      <v-spacer></v-spacer>
      <v-btn @click="$router.push('/login')" text
        ><span class="hidden-sm-and-down">Log in</span>
        <v-icon class="ml-2">mdi-account-circle-outline</v-icon>
      </v-btn>
    </v-app-bar>

    <v-content>
      <router-view></router-view>
    </v-content>
    <v-footer>
      <v-switch
        v-model="$vuetify.theme.dark"
        label="Switch to Dark Mode"
      ></v-switch>
    </v-footer>
  </v-app>
</template>

<script>
export default {
  name: "App",

  components: {},

  data: () => ({
    //
  })
};
</script>

<style></style>
