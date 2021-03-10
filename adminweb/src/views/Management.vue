<template>
  <v-container id="manage">
    <v-row>
      <v-col cols="12">
        <v-card class="mt-5">
          <management-room-type />
          <management-meeting-room />
        </v-card>
        <management-package-2 />
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import ManagementMeetingRoom from "../components/ManagementMeetingRoom.vue";
import ManagementPackage2 from "../components/ManagementPackage2.vue";
import ManagementRoomType from "../components/ManagementRoomType.vue";

export default {
  name: "manage",

  components: {
    ManagementPackage2,
    ManagementRoomType,
    ManagementMeetingRoom
  }
};
</script>

<style></style>
