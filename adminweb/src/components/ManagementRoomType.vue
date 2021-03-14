<template>
  <v-container fluid>
    <v-card outlined>
      <v-card-title primary-title>
        ประเภทห้องประชุม
      </v-card-title>
      <v-container class="d-flex align-content-start flex-wrap">
        <v-card
          v-for="item in roomtypedata"
          :key="'type' + item"
          outlined
          width="240px"
          height="240px"
          class="mb-4 mx-2"
        >
          <v-container>
            <v-card-title primary-title>
              {{ item.name }} <v-spacer></v-spacer>
            </v-card-title>
            <v-card-text>
              <v-container
                ><v-row><span>รายละเอียด</span></v-row>
                <v-row>
                  <span>{{ item.detail ? item.detail : "-" }}</span>
                </v-row>
                <v-row
                  ><span>ราคา: {{ item.price }} ฿/hr</span></v-row
                ></v-container
              >
            </v-card-text>
            <v-footer class="justify-center">
              <v-card-actions>
                <v-btn @click="editItem(item)" icon
                  ><v-icon style="color: #9CCC65">mdi-pencil</v-icon></v-btn
                >
                <v-btn @click="deleteItem(item)" icon
                  ><v-icon style="color: #B71C1C">mdi-delete</v-icon></v-btn
                >
              </v-card-actions>
            </v-footer>
          </v-container>
        </v-card>

        <v-card outlined width="240px" height="240px" class="mb-4 mx-2">
          <v-dialog v-model="dialog" max-width="500px">
            <template v-slot:activator="{ on, attrs }">
              <v-btn x-large v-bind="attrs" v-on="on" width="100%" height="100%"
                ><v-icon size="50">mdi-plus-box</v-icon></v-btn
              >
            </template>
            <v-card>
              <v-card-title primary-title>
                {{ formTitle }}
              </v-card-title>
              <v-card-text>
                <v-text-field
                  label="ชื่อประเภท"
                  v-model="roomtypeItem.name"
                  required
                ></v-text-field>
              </v-card-text>
              <v-card-text>
                <v-textarea
                  v-model="roomtypeItem.detail"
                  label="รายละเอียด"
                  outlined
                ></v-textarea>
              </v-card-text>
              <v-card-text>
                <v-text-field
                  v-model="roomtypeItem.price"
                  label="ราคา"
                  suffix="บาท"
                  type="number"
                  required
                ></v-text-field>
              </v-card-text>

              <v-card-actions>
                <v-spacer></v-spacer>

                <v-btn text @click="close"> Close </v-btn>
                <v-btn color="primary" text @click="save">
                  Save
                </v-btn>
              </v-card-actions>
            </v-card>
          </v-dialog>
        </v-card>
      </v-container>
    </v-card>
  </v-container>
</template>

<script>
import axios from "axios";

export default {
  data: function() {
    return {
      dialog: false,
      roomtypeIndex: -1,
      roomtypedata: [],
      roomtypeItem: {
        name: "",
        detail: "",
        price: ""
      },
      defaultItem: {
        name: "",
        detail: "",
        price: ""
      }
    };
  },

  computed: {
    formTitle() {
      return this.roomtypeIndex === -1 ? "New Item" : "Edit Item";
    }
  },
  created() {
    this.showroomtypedata();
  },
  methods: {
    async showroomtypedata() {
      var roomtypedata = await axios.get("meetingroom/type/");

      if (roomtypedata != null) {
        this.roomtypedata = roomtypedata.data;
      } else {
        return [];
      }
    },

    editItem: function(item) {
      this.roomtypeIndex = this.roomtypedata.indexOf(item);
      this.roomtypeItem = Object.assign({}, item);
      this.dialog = true;
    },

    async deleteItem(item) {
      this.roomtypeIndex = this.roomtypedata.indexOf(item);
      await axios.delete(
        `meetingroom/type/${this.roomtypedata[this.roomtypeIndex].id}/`
      );

      this.showroomtypedata();
      this.close();
    },

    async save() {
      if (this.roomtypeIndex > -1) {
        await axios.put(
          `meetingroom/type/${this.roomtypedata[this.roomtypeIndex].id}/`,
          this.roomtypeItem
        );
      } else {
        await axios.post("meetingroom/type/", this.roomtypeItem);
      }

      this.showroomtypedata();
      this.close();
      this.$forceUpdate();
    },

    close() {
      this.dialog = false;
      this.$nextTick(() => {
        this.roomtypeItem = Object.assign({}, this.defaultItem);
        this.roomtypeIndex = -1;
      });
    }
  }
};
</script>
