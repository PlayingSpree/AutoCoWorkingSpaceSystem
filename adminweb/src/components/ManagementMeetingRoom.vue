<template>
  <v-container fluid>
    <v-card-title primary-title>
      ห้องประชุม
    </v-card-title>
    <v-container d-flex align-content-start flex-wrap>
      <v-card
        v-for="item in roomnamedata"
        :key="'meeting' + item"
        outlined
        width="300px"
        height="400px"
        class="mx-2"
      >
        <v-card-title>
          {{ item.name }} <v-spacer></v-spacer
          ><v-btn @click="editItem(item)" icon
            ><v-icon style="color: #9CCC65">mdi-pencil</v-icon></v-btn
          ><v-btn @click="deleteItem(item)" icon
            ><v-icon style="color: #B71C1C">mdi-delete</v-icon></v-btn
          >
        </v-card-title>
        <v-card-text>
          ประเภทห้อง
          <v-select
            v-model="item.type_detail.name"
            :items="roomtypename"
            @input="setroomtype(item.type_detail.name, item)"
            solo
          ></v-select>
          สถานะ
          <v-select
            v-model="item.status"
            :items="status"
            @change="setroomstatus(item.status, item)"
            solo
          ></v-select>
        </v-card-text>
        <v-card-actions class="justify-center">
          <v-btn block @click="editIot(item.id)" v-bind="attrs" v-on="on">
            ตั้งค่าห้องประชุม
          </v-btn>
        </v-card-actions>
      </v-card>

      <v-dialog v-model="dialogiot" max-width="600px">
        <v-card>
          <v-card-title>
            จัดการห้องประชุม
          </v-card-title>
          <v-card-text>
            <span
              >status:
              <v-icon :color="iotItem.status ? 'green' : 'red'" x-small
                >mdi-circle</v-icon
              ></span
            >
            <v-text-field
              v-model="iotItem.iot_ip"
              label="for IOT"
              prefix="IP : "
              :rules="[() => !!iotItem.iot_ip || 'This field is required']"
              :ref="iotItem.iot_ip"
            ></v-text-field>
            <v-text-field
              v-model="iotItem.door_ip"
              label="for Door"
              prefix="IP : "
              :rules="[() => !!iotItem.door_ip || 'This field is required']"
              :ref="iotItem.door_ip"
            ></v-text-field>
          </v-card-text>
          <template v-if="iotItem.status">
            <v-card-title>
              หลอดไฟ
            </v-card-title>
            <v-card-text>
              <v-container>
                <v-row class="d-flex align-center">
                  <v-col cols="3">
                    <span>ความสว่าง</span>
                  </v-col>
                  <v-btn
                    class="mx-2"
                    color="blue-grey lighten-5"
                    @click="setroomlight('down')"
                    ><v-icon color="black">mdi-arrow-left-bold</v-icon></v-btn
                  >
                  <v-btn
                    class="mx-2"
                    color="blue-grey darken-3"
                    @click="setroomlight('up')"
                    ><v-icon>mdi-arrow-right-bold</v-icon></v-btn
                  >
                </v-row>
                <v-row class="d-flex align-center">
                  <v-col cols="3">
                    <span>เปิด/ปิด</span>
                  </v-col>
                  <v-btn
                    class="mx-2"
                    :color="iotItem.light_power ? 'success' : 'red darken-4'"
                    @click="power_light()"
                    >{{ iotItem.light_power ? "on" : "off" }}</v-btn
                  >
                </v-row>
              </v-container>
            </v-card-text>
            <v-card-title>
              เครื่องปรับอากาศ
            </v-card-title>
            <v-card-text>
              <v-container>
                <v-row class="d-flex align-center">
                  <v-col cols="3">
                    <span>อุณหภูมิ</span>
                  </v-col>
                  <v-btn
                    class="mx-2"
                    color="light-blue lighten-2"
                    @click="setroomtemp('down')"
                    ><v-icon>mdi-minus</v-icon></v-btn
                  >
                  <span>{{ iotItem.temp }}</span>
                  <v-btn
                    class="mx-2"
                    color="pink lighten-1"
                    @click="setroomtemp('up')"
                    ><v-icon>mdi-plus</v-icon></v-btn
                  >
                </v-row>
                <v-row class="d-flex align-center">
                  <v-col cols="3">
                    <span>เปิด/ปิด</span>
                  </v-col>
                  <v-btn
                    class="mx-2"
                    :color="iotItem.air_power ? 'success' : 'red darken-4'"
                    @click="power_air()"
                    >{{ iotItem.air_power ? "on" : "off" }}</v-btn
                  >
                </v-row>
              </v-container>
            </v-card-text>
          </template>
          <v-card-actions>
            <v-spacer></v-spacer>
            <v-btn text @click="closeiot"> Close </v-btn>
            <v-btn color="primary" text @click="saveiot">
              Save
            </v-btn>
          </v-card-actions>
        </v-card>
      </v-dialog>

      <v-card outlined width="300px" height="400px" class="mx-2">
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
                v-model="roomnameItem.name"
                label="ชื่อห้อง"
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
  </v-container>
</template>

<script>
import axios from "axios";

export default {
  data: function() {
    return {
      formHasErrors: false,
      dialog: false,
      dialogiot: false,
      roomnameIndex: -1,
      roomnamedata: [],
      roomtypename: [],
      roomtypedata: [],
      iotdata: {},
      iotip: {},
      status: ["ปิดปรับปรุง", "เปิดให้บริการ"],
      roomnameItem: {
        id: "",
        name: "",
        detail: "",
        status: "",
        type: "",
        type_detail: {},
        is_active: false
      },
      defaultItem: {
        id: "",
        name: "",
        detail: "",
        status: "",
        type: "",
        type_detail: {},
        is_active: false
      },
      iotItem: {
        room_id: "",
        iot_ip: "",
        door_ip: "",
        status: false,
        color: 0,
        brightness_up: false,
        brightness_down: false,
        light_power: false,
        temp: 25,
        air_power: false
      },
      defaultiot: {
        room_id: "",
        iot_ip: "",
        door_ip: "",
        status: false,
        color: 0,
        brightness_up: false,
        brightness_down: false,
        light_power: false,
        temp: 25,
        air_power: false
      }
    };
  },
  watch: {
    dialogiot(val) {
      val || this.closeiot();
    }
  },
  computed: {
    formTitle() {
      return this.roomnameIndex === -1 ? "New Item" : "Edit Item";
    }
  },
  created() {
    this.showroomnamedata();
    this.allroomtype();
  },
  methods: {
    async showroomnamedata() {
      var roomnamedata = await axios.get("meetingroom/");

      this.roomnamedata = roomnamedata.data;

      for (var i = 0; i < this.roomnamedata.length; i++) {
        if (this.roomnamedata[i].type_detail == null) {
          this.roomnamedata[i].type_detail = {
            name: ""
          };
        }
        if (this.roomnamedata[i].is_active == true) {
          this.roomnamedata[i].status = "เปิดให้บริการ";
        } else {
          this.roomnamedata[i].status = "ปิดปรับปรุง";
        }
      }
    },

    async editIot(room_id) {
      this.dialogiot = true;
      let checkroomstatus = null;

      await axios
        .get(`iot/room/setup/${room_id}/`)
        .then(response => {
          this.iotip = response.data;
        })
        .catch(error => (checkroomstatus = error.response.data));

      await axios
        .get(`iot/room/${room_id}/`)
        .then(responese => (this.iotdata = responese.data))
        .catch(error => (checkroomstatus = error.response.data));

      this.iotItem.room_id = room_id;
      if (checkroomstatus == null) {
        this.iotItem.iot_ip = this.iotip.iot_ip;
        this.iotItem.door_ip = this.iotip.door_ip;
        this.iotItem.status = true;
        this.iotItem.color = this.iotdata[1].data.color;
        this.iotItem.brightness_up = false;
        this.iotItem.brightness_down = false;
        this.iotItem.light_power = this.iotdata[1].data.power;
        this.iotItem.temp = this.iotdata[0].data.temp;
        this.iotItem.air_power = this.iotdata[0].data.power;
      } else {
        this.iotItem.status = false;
        this.iotItem.iot_ip = this.iotip.iot_ip;
        this.iotItem.door_ip = this.iotip.door_ip;
      }
    },

    async saveiot() {
      this.iotip.iot_ip = this.iotItem.iot_ip;
      this.iotip.door_ip = this.iotItem.door_ip;
      await axios.put(`iot/room/setup/${this.iotItem.room_id}/`, this.iotip);
      this.closeiot();
    },

    closeiot() {
      this.dialogiot = false;
      this.$nextTick(() => {
        this.iotItem = Object.assign({}, this.defaultiot);
        this.iotdata = Object.assign({}, {});
        this.iotip = Object.assign({}, {});
      });
    },

    editItem: function(item) {
      this.roomnameIndex = this.roomnamedata.indexOf(item);
      this.roomnameItem = Object.assign({}, item);
      this.dialog = true;
    },

    async deleteItem(item) {
      this.roomnameIndex = this.roomnamedata.indexOf(item);

      await axios.delete(
        `meetingroom/${this.roomnamedata[this.roomnameIndex].id}/`
      );

      this.showroomnamedata();
      this.close();
    },

    async save() {
      if (this.roomnameIndex > -1) {
        await axios.put(
          `meetingroom/${this.roomnamedata[this.roomnameIndex].id}/`,
          this.roomnameItem
        );
      } else {
        await axios.post("meetingroom/", this.roomnameItem);
      }
      this.showroomnamedata();
      this.close();
    },

    close() {
      this.dialog = false;
      this.$nextTick(() => {
        this.roomnameItem = Object.assign({}, this.defaultItem);
        this.roomnameIndex = -1;
      });
    },

    async allroomtype() {
      var alltype = [];
      var roomtypedata = await axios.get("meetingroom/type/");

      for (var i = 0; i < roomtypedata.data.length; i++) {
        alltype.push(roomtypedata.data[i].name);
      }
      this.roomtypename = alltype;
      this.roomtypedata = roomtypedata.data;
    },

    async setroomtype(type, item) {
      this.allroomtype();
      this.roomnameIndex = this.roomnamedata.indexOf(item);
      this.roomnameItem = Object.assign({}, item);
      for (var i = 0; i < this.roomtypedata.length; i++) {
        if (this.roomtypedata[i].name == type) {
          this.roomnameItem.type_detail.name = this.roomtypedata[i];
          this.roomnameItem.type = this.roomtypedata[i].id;
        }
      }

      await axios.put(
        `meetingroom/${this.roomnamedata[this.roomnameIndex].id}/`,
        this.roomnameItem
      );
      this.close();
      this.showroomnamedata();
    },

    async setroomstatus(status, item) {
      let active = false;
      if (status == "เปิดให้บริการ") {
        active = true;
      } else {
        active = false;
      }
      this.roomnameIndex = this.roomnamedata.indexOf(item);
      this.roomnameItem = Object.assign({}, item);
      this.roomnameItem.is_active = active;

      await axios.put(
        `meetingroom/${this.roomnamedata[this.roomnameIndex].id}/`,
        this.roomnameItem
      );
      this.close();
      this.showroomnamedata();
    },

    async setroomlight(type) {
      if (type == "up") {
        this.iotdata[1].data.brightness_up = true;
        this.iotdata[1].data.power = true;
        await axios.put(`iot/room/${this.iotItem.room_id}/`, {
          iot_id: 2,
          data: this.iotdata[1].data
        });
      } else {
        this.iotdata[1].data.brightness_down = true;
        this.iotdata[1].data.power = true;
        await axios.put(`iot/room/${this.iotItem.room_id}/`, {
          iot_id: 2,
          data: this.iotdata[1].data
        });
      }
    },

    async setroomtemp(type) {
      if (
        type == "up" &&
        this.iotItem.temp < this.iotdata[0].data_info.temp.max
      ) {
        this.iotItem.temp += 1;
        this.iotdata[0].data.temp += 1;
        await axios.put(`iot/room/${this.iotItem.room_id}/`, {
          iot_id: 1,
          data: this.iotdata[0].data
        });
      } else if (
        type == "down" &&
        this.iotItem.temp > this.iotdata[0].data_info.temp.min
      ) {
        this.iotItem.temp -= 1;
        this.iotdata[0].data.temp -= 1;
        await axios.put(`iot/room/${this.iotItem.room_id}/`, {
          iot_id: 1,
          data: this.iotdata[0].data
        });
      }
    },

    async power_air() {
      this.iotItem.air_power = !this.iotItem.air_power;
      this.iotdata[0].data.power = this.iotItem.air_power;
      await axios.put(`iot/room/${this.iotItem.room_id}/`, {
        iot_id: 1,
        data: this.iotdata[0].data
      });
    },

    async power_light() {
      this.iotItem.light_power = !this.iotItem.light_power;
      this.iotdata[1].data.brightness_up = false;
      this.iotdata[1].data.brightness_down = false;
      this.iotdata[1].data.power = this.iotItem.light_power;
      await axios.put(`iot/room/${this.iotItem.room_id}/`, {
        iot_id: 2,
        data: this.iotdata[1].data
      });
    }
  }
};
</script>
