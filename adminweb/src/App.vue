<template>
  <v-app>
    <v-app-bar app>
      <template v-if="authenicated">
        <v-btn @click="$router.push('/dashboard')" text>Dashboard</v-btn>
        <v-btn @click="$router.push('/manage')" text>Management</v-btn>
        <v-btn @click="$router.push('/review')" text>Review</v-btn>
        <v-btn @click="$router.push('/report')" text>Report</v-btn>
        <v-btn @click="$router.push('/user')" text>User</v-btn>
        <v-spacer></v-spacer>
        <span class="hidden-sm-and-down">{{ user.email }}</span>
        <v-btn @click="signOut" icon><v-icon>mdi-logout</v-icon></v-btn>
      </template>
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
import { mapGetters, mapActions } from "vuex";

export default {
  name: "App",

  components: {},

  data: () => ({
    //
  }),

  computed: {
    ...mapGetters({
      authenicated: "auth/authenicated",
      user: "auth/user"
    })
  },

  methods: {
    ...mapActions({
      signOutAction: "auth/signOut"
    }),

    signOut() {
      this.signOutAction().then(() => {
        this.$router.replace({
          name: "Login"
        });
      });
    }
  }
};
</script>

<style></style>
