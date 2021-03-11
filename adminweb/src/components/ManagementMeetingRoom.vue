<template>
  <v-container fluid>
    <v-card-title primary-title>
      ห้องประชุม
    </v-card-title>
    <v-card
      v-for="item in roomnamedata"
      :key="'meeting' + item"
      outlined
      class="my-2 align-center"
    >
      <v-container fluid>
        <v-row>
          <v-col cols="2">
            <v-card elevation="0">
              <v-card-title>
                {{ item.name }}
              </v-card-title>
              <v-card-text>
                ประเภทห้อง
              </v-card-text>
              <v-select
                v-model="item.type"
                :items="roomtypedata"
                @input="setroomtype(item.type, item)"
                solo
              ></v-select>
              <v-card-text>
                สถานะ
              </v-card-text>
              <v-select
                v-model="item.status"
                :items="status"
                @input="setroomstatus(item.status, item)"
                solo
              ></v-select>
            </v-card>
          </v-col>
          <v-divider vertical></v-divider>
          <v-col cols="5"
            ><v-card width="400px" elevation="0">
              <v-card-title>
                หลอดไฟ
              </v-card-title>
              <v-card-text class="mb-4">
                สีไฟ
              </v-card-text>
              <v-row class="mb-8" no-gutters>
                <v-col>
                  <v-btn
                    color="white"
                    width="100px"
                    @click="setRoomLightColor(0, item)"
                    ><v-icon style="color: #000000">{{
                      item.lightColor == 0 ? "mdi-check" : ""
                    }}</v-icon></v-btn
                  >
                </v-col>
                <v-col>
                  <v-btn
                    color="amber lighten-5"
                    width="100px"
                    @click="setRoomLightColor(1, item)"
                    style="color: #000000"
                    ><v-icon style="color: #000000">{{
                      item.lightColor == 1 ? "mdi-check" : ""
                    }}</v-icon></v-btn
                  >
                </v-col>
                <v-col>
                  <v-btn
                    color="orange lighten-3"
                    width="100px"
                    @click="setRoomLightColor(2, item)"
                    ><v-icon style="color: #000000">
                      {{ item.lightColor == 2 ? "mdi-check" : "" }}</v-icon
                    ></v-btn
                  >
                </v-col>
              </v-row>
              <v-card-text class="mb-4">
                ความสว่าง
              </v-card-text>
              <v-row no-gutters>
                <v-col>
                  <v-btn
                    color="white"
                    width="50px"
                    @click="setRoomLightBright(0, item)"
                    ><v-icon style="color: #000000">
                      {{ item.brightness == 0 ? "mdi-check" : "" }}</v-icon
                    ></v-btn
                  >
                </v-col>
                <v-col>
                  <v-btn
                    color="grey lighten-2"
                    width="50px"
                    @click="setRoomLightBright(1, item)"
                    ><v-icon style="color: #000000">
                      {{ item.brightness == 1 ? "mdi-check" : "" }}</v-icon
                    ></v-btn
                  >
                </v-col>
                <v-col>
                  <v-btn
                    color="grey lighten-1"
                    width="50px"
                    @click="setRoomLightBright(2, item)"
                    ><v-icon style="color: #000000">
                      {{ item.brightness == 2 ? "mdi-check" : "" }}</v-icon
                    ></v-btn
                  >
                </v-col>
                <v-col>
                  <v-btn
                    color="grey darken-1"
                    width="50px"
                    @click="setRoomLightBright(3, item)"
                    ><v-icon style="color: #000000">
                      {{ item.brightness == 3 ? "mdi-check" : "" }}</v-icon
                    ></v-btn
                  >
                </v-col>
                <v-col>
                  <v-btn
                    color="grey darken-2"
                    width="50px"
                    @click="setRoomLightBright(4, item)"
                    ><v-icon style="color: #000000">
                      {{ item.brightness == 4 ? "mdi-check" : "" }}</v-icon
                    ></v-btn
                  >
                </v-col>
              </v-row>
            </v-card></v-col
          >
          <v-divider vertical></v-divider>
          <v-col class="align-center"
            ><v-card elevation="0">
              <v-card-title>
                เครื่องปรับอากาศ
              </v-card-title>
              <v-card-text>
                อุณหภูมิ
              </v-card-text>
              <v-container class="d-flex align-content-start mb-4">
                <v-btn
                  color="light-blue lighten-2"
                  class="mr-5"
                  @click="setRoomTempDown(item)"
                  ><v-icon>mdi-minus</v-icon></v-btn
                >
                <p class="mr-5" style="font-size: 20px">
                  {{ item.temp }}
                </p>
                <v-btn color="pink lighten-1" @click="setRoomTempUp(item)"
                  ><v-icon>mdi-plus</v-icon></v-btn
                >
              </v-container>
              <v-card-text class="mb-4">
                เปิด/ปิด
              </v-card-text>
              <v-btn
                class="ml-3"
                :color="item.air ? 'success' : 'red darken-4'"
                @click="setRoomAir(item)"
                >{{ item.air ? "on" : "off" }}</v-btn
              >
            </v-card></v-col
          >
          <v-btn @click="editItem(item)" icon
            ><v-icon style="color: #9CCC65">mdi-pencil</v-icon></v-btn
          >
          <v-btn @click="deleteItem(item)" icon
            ><v-icon style="color: #B71C1C">mdi-delete</v-icon></v-btn
          >
        </v-row>
      </v-container>
    </v-card>
    <v-card outlined height="338px" class="my-2">
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
</template>

<script>
export default {
  data: function() {
    return {
      dialog: false,
      roomnameIndex: -1,
      roomnamedata: [],
      roomtypedata: [],
      status: ["ปิดปรับปรุง", "เปิดให้บริการ"],
      roomnameItem: {
        name: "",
        type: "",
        status: "ปิดปรับปรุง",
        lightColor: 0,
        brightness: 0,
        temp: 25,
        air: false
      },
      defaultItem: {
        name: "",
        type: "",
        status: "ปิดปรับปรุง",
        lightColor: 0,
        brightness: 0,
        temp: 25,
        air: false
      }
    };
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
    showroomnamedata: function() {
      var roomnamedata = JSON.parse(localStorage.getItem("roomnamedata"));

      if (roomnamedata != null) {
        this.roomnamedata = roomnamedata;
      } else {
        return [];
      }
    },

    editItem: function(item) {
      this.roomnameIndex = this.roomnamedata.indexOf(item);
      this.roomnameItem = Object.assign({}, item);
      this.dialog = true;
    },

    deleteItem: function(item) {
      var roomnamedata = JSON.parse(localStorage.getItem("roomnamedata"));
      this.roomnameIndex = this.roomnamedata.indexOf(item);
      this.roomnameItem = Object.assign({}, item);
      roomnamedata.splice(this.roomnameIndex, 1);
      localStorage.setItem("roomnamedata", JSON.stringify(roomnamedata));
      this.$nextTick(() => {
        this.roomnameItem = Object.assign({}, this.defaultItem);
        this.roomnameIndex = -1;
      });
      this.showroomnamedata();
    },

    save: function() {
      if (localStorage.getItem("roomnamedata") == null) {
        localStorage.setItem("roomnamedata", "[]");
      }

      var old_name = JSON.parse(localStorage.getItem("roomnamedata"));

      if (this.roomnameIndex > -1) {
        Object.assign(old_name[this.roomnameIndex], this.roomnameItem);
      } else {
        old_name.push(this.roomnameItem);
      }

      localStorage.setItem("roomnamedata", JSON.stringify(old_name));
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

    allroomtype() {
      var alltype = [];
      var roomtypedata = JSON.parse(localStorage.getItem("roomtypedata"));

      for (var i = 0; i < roomtypedata.length; i++) {
        alltype.push(roomtypedata[i].name);
      }
      this.roomtypedata = alltype;
      this.showroomnamedata();
    },

    setroomtype(type, item) {
      var roomnamedata = JSON.parse(localStorage.getItem("roomnamedata"));
      this.roomnameIndex = this.roomnamedata.indexOf(item);
      roomnamedata[this.roomnameIndex].type = type;
      localStorage.setItem("roomnamedata", JSON.stringify(roomnamedata));
      console.log(roomnamedata.type);
      this.close();
      this.showroomnamedata();
    },

    setroomstatus(status, item) {
      var roomnamedata = JSON.parse(localStorage.getItem("roomnamedata"));
      this.roomnameIndex = this.roomnamedata.indexOf(item);
      roomnamedata[this.roomnameIndex].status = status;
      localStorage.setItem("roomnamedata", JSON.stringify(roomnamedata));
      this.close();
      this.showroomnamedata();
    },

    setRoomLightColor(color, item) {
      var roomnamedata = JSON.parse(localStorage.getItem("roomnamedata"));
      this.roomnameIndex = this.roomnamedata.indexOf(item);
      roomnamedata[this.roomnameIndex].lightColor = color;
      localStorage.setItem("roomnamedata", JSON.stringify(roomnamedata));
      this.showroomnamedata();
      this.$forceUpdate();
    },

    setRoomLightBright(bright, item) {
      var roomnamedata = JSON.parse(localStorage.getItem("roomnamedata"));
      this.roomnameIndex = this.roomnamedata.indexOf(item);
      roomnamedata[this.roomnameIndex].brightness = bright;
      localStorage.setItem("roomnamedata", JSON.stringify(roomnamedata));
      this.showroomnamedata();
      this.$forceUpdate();
    },

    setRoomTempUp: function(item) {
      var roomnamedata = JSON.parse(localStorage.getItem("roomnamedata"));
      this.roomnameIndex = this.roomnamedata.indexOf(item);
      roomnamedata[this.roomnameIndex].temp += 1;
      localStorage.setItem("roomnamedata", JSON.stringify(roomnamedata));
      this.showroomnamedata();
    },

    setRoomTempDown: function(item) {
      var roomnamedata = JSON.parse(localStorage.getItem("roomnamedata"));
      this.roomnameIndex = this.roomnamedata.indexOf(item);
      roomnamedata[this.roomnameIndex].temp -= 1;
      localStorage.setItem("roomnamedata", JSON.stringify(roomnamedata));
      this.showroomnamedata();
    },

    setRoomAir: function(item) {
      var roomnamedata = JSON.parse(localStorage.getItem("roomnamedata"));
      this.roomnameIndex = this.roomnamedata.indexOf(item);
      roomnamedata[this.roomnameIndex].air = !roomnamedata[this.roomnameIndex]
        .air;
      localStorage.setItem("roomnamedata", JSON.stringify(roomnamedata));
      this.showroomnamedata();
    }
  }
};
</script>
