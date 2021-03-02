<template>
  <v-container id="manage">
    <v-row>
      <v-col cols="12">
        <management-room />
        <management-package />
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import ManagementRoom from "../components/ManagementRoom.vue";
import ManagementPackage from "../components/ManagementPackage.vue";

export default {
  name: "manage",

  components: {
    ManagementRoom,
    ManagementPackage
  }
};
</script>

<style></style>
