<template>
  <v-container id="manage">
    <v-row>
      <v-col cols="12">
        <management-room />
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import ManagementRoom from "../components/ManagementRoom.vue";

export default {
  name: "manage",

  components: {
    ManagementRoom
  }
};
</script>

<style></style>
