<template>
  <v-app>
    <v-app-bar app color="white" dark>
      <v-btn @click="$router.push('/')" text color="black">Dashboard</v-btn>
      <v-btn @click="$router.push('/manage')" text color="black"
        >Management</v-btn
      >
      <v-btn @click="$router.push('/login')" text color="black">Review</v-btn>
      <v-btn @click="$router.push('/login')" text color="black">Report</v-btn>
      <v-btn @click="$router.push('/login')" text color="black">User</v-btn>
      <v-spacer></v-spacer>
      <v-btn @click="$router.push('/login')" text color="black"
        ><span class="hidden-sm-and-down">Log in</span>
        <v-icon class="ml-2">mdi-account-circle-outline</v-icon>
      </v-btn>
    </v-app-bar>
    <v-content>
      <router-view></router-view>
    </v-content>
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
