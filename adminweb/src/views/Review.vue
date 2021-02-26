<template>
  <v-container>
    <dashboard-download />
  </v-container>
</template>

<script>
import DashboardDownload from "../components/DashboardDownload.vue";

export default {
    name: "review",
    components: {
        DashboardDownload
    }
}
</script>
