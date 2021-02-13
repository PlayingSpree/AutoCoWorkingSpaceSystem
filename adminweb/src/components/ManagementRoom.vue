<template>
  <v-card>
    <v-card-title primary-title>
      ประเภทห้องประชุม
    </v-card-title>
    <v-row>
      <v-col cols="2">
        <v-menu
          v-model="menu"
          :close-on-content-click="false"
          :nudge-width="200"
          offset-x
        >
          <template v-slot:activator="{ on, attrs }">
            <v-btn icon x-large v-bind="attrs" v-on="on"
              ><v-icon>mdi-plus-box</v-icon></v-btn
            >
          </template>

          <v-card>
            <v-list>
              <v-list-item>
                <v-list-item-action>
                  <v-overflow-btn
                    class="my-2"
                    :items="roomSize"
                    label="ขนาดห้อง"
                    editable
                  ></v-overflow-btn>
                </v-list-item-action>
              </v-list-item>

              <v-list-item>
                <v-list-tile-title class="mr-2"
                  >จำนวนคนสูงสุด :</v-list-tile-title
                >
                <v-list-tile-action>
                  <v-text-field
                    v-model="numUserSlider"
                    class="mt-0 pt-0"
                    hide-details
                    single-line
                    type="number"
                    style="width: 40px"
                  ></v-text-field>
                </v-list-tile-action>
                <v-list-tile-title>คน</v-list-tile-title>
              </v-list-item>

              <v-list-item>
                <v-list-tile-title class="mr-2">ราคา :</v-list-tile-title>
                <v-list-tile-action>
                  <v-text-field
                    v-model="roomPrice"
                    class="mt-0 pt-0"
                    hide-details
                    single-line
                    type="number"
                    style="width: 50px"
                  ></v-text-field>
                </v-list-tile-action>
                <v-list-tile-title>บาท/ชม.</v-list-tile-title>
              </v-list-item>
            </v-list>

            <v-card-actions>
              <v-spacer></v-spacer>

              <v-btn text @click="menu = false">
                Cancel
              </v-btn>
              <v-btn color="primary" text @click="menu = false">
                Save
              </v-btn>
            </v-card-actions>
          </v-card>
        </v-menu>
      </v-col>
    </v-row>
  </v-card>
</template>

<script>
export default {
  data: function() {
    return {
      roomSize: ["ห้องเล็ก", "ห้องกลาง", "ห้องใหญ่"],
      numUserSlider: 10,
      roomPrice: 200,
      menu: false
    };
  }
};
</script>

<style></style>
