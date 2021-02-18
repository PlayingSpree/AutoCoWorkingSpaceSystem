<template>
  <v-card>
    <v-container fluid>
      <v-card outlined>
        <v-container fluid>
          <v-row
            ><v-card-title style="font-size:20px">
              ประเภทห้องประชุม
            </v-card-title></v-row
          >

          <v-row>
            <v-container class="d-flex align-content-start flex-wrap">
              <v-card
                outlined
                v-for="[key, item] in Object.entries(roomTypeDetail())"
                :key="key"
                :id="key"
                width="240px"
                height="240px"
                class="mb-4 mx-2"
              >
                <v-card-title class="justify-center">
                  {{ key }} <v-spacer></v-spacer>
                  <v-tooltip bottom class="ml-3">
                    <template v-slot:activator="{ on, attrs }">
                      <v-icon v-bind="attrs" v-on="on" small
                        >mdi-information</v-icon
                      >
                    </template>
                    <span>{{ item[2] }}</span>
                  </v-tooltip>
                </v-card-title>
                <v-card-text> จำนวนคนสูงสุด: {{ item[0] }} </v-card-text>
                <v-card-text> ราคา: {{ item[1] }} ฿/hr </v-card-text>
                <v-card-actions class="justify-center">
                  <v-btn icon
                    ><v-icon style="color: #9CCC65">mdi-pencil</v-icon></v-btn
                  >
                  <v-btn @click="deleteRoomType(key)" icon
                    ><v-icon style="color: #B71C1C">mdi-delete</v-icon></v-btn
                  >
                </v-card-actions>
              </v-card>
              <v-card outlined width="240px" height="240px" class="mb-4 mx-2">
                <v-menu
                  v-model="menu"
                  :close-on-content-click="false"
                  :nudge-width="100"
                  max-width="300px"
                  offset-x
                  transition="slide-x-transition"
                >
                  <template v-slot:activator="{ on, attrs }">
                    <v-btn
                      x-large
                      v-bind="attrs"
                      v-on="on"
                      width="100%"
                      height="100%"
                      ><v-icon size="50">mdi-plus-box</v-icon></v-btn
                    >
                  </template>

                  <v-card>
                    <v-list>
                      <v-list-item>
                        <v-list-item-action>
                          <v-text-field
                            label="ชื่อห้อง"
                            v-model="roomtype"
                            id="inputtype"
                          ></v-text-field>
                        </v-list-item-action>
                      </v-list-item>

                      <v-list-item>
                        <v-list-tile-action>
                          <v-textarea
                            name="describtion"
                            label="คำอธิบายห้อง"
                            id="inputdetail"
                            outlined
                          ></v-textarea>
                        </v-list-tile-action>
                      </v-list-item>

                      <v-list-item>
                        <v-list-tile-title class="mr-2"
                          >จำนวนคนสูงสุด :</v-list-tile-title
                        >
                        <v-list-tile-action>
                          <v-text-field
                            v-model="numUserSlider"
                            id="inputuser"
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
                        <v-list-tile-title class="mr-2"
                          >ราคา :</v-list-tile-title
                        >
                        <v-list-tile-action>
                          <v-text-field
                            v-model="roomPrice"
                            id="inputprice"
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
                      <v-btn color="primary" text @click="addTypeData">
                        OK
                      </v-btn>
                    </v-card-actions>
                  </v-card>
                </v-menu>
              </v-card>
            </v-container>
          </v-row>
        </v-container>
      </v-card>
      <v-card-title style="font-size:20px">
        ห้องประชุม
      </v-card-title>

      <v-card
        v-for="key in Object.keys(allroomname())"
        :key="key"
        outlined
        class="my-2 align-center"
      >
        <v-container fluid>
          <v-row>
            <v-col cols="2">
              <v-card elevation="0">
                <v-card-title>
                  {{ key }}
                </v-card-title>
                <v-card-text>
                  ประเภทห้อง
                </v-card-text>
                <v-select
                  v-model="select"
                  :placeholder="allroomname()[key][0]"
                  :items="getRoomtype()"
                  full-width="100px"
                  @input="setRoomType(select, key)"
                  solo
                ></v-select>
                <v-card-text>
                  สถานะ
                </v-card-text>
                <v-select
                  v-model="selectstatus"
                  :placeholder="allroomname()[key][1]"
                  :items="status"
                  full-width="100px"
                  @input="setRoomStatus(selectstatus, key)"
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
              </v-card></v-col
            >
            <v-divider vertical></v-divider>
            <v-col
              ><v-card width="300px" elevation="0">
                <v-card-title>
                  เครื่องปรับอากาศ
                </v-card-title>
              </v-card></v-col
            >
          </v-row>
        </v-container>
      </v-card>
      <v-card outlined height="338px" class="my-2">
        <v-menu
          v-model="menumeeting"
          :close-on-content-click="false"
          :nudge-width="100"
          max-width="300px"
          offset-x
          transition="slide-x-transition"
        >
          <template v-slot:activator="{ on, attrs }">
            <v-btn x-large v-bind="attrs" v-on="on" width="100%" height="100%"
              ><v-icon size="50">mdi-plus-box</v-icon></v-btn
            >
          </template>

          <v-card>
            <v-list>
              <v-list-item>
                <v-list-item-action>
                  <v-text-field
                    label="ชื่อห้องประชุม"
                    v-model="roomname"
                    id="inputname"
                  ></v-text-field>
                </v-list-item-action>
              </v-list-item>
            </v-list>

            <v-card-actions>
              <v-spacer></v-spacer>

              <v-btn text @click="menumeeting = false">
                Cancel
              </v-btn>
              <v-btn color="primary" text @click="addroom">
                OK
              </v-btn>
            </v-card-actions>
          </v-card>
        </v-menu>
      </v-card>
    </v-container>
  </v-card>
</template>

<script>
export default {
  data: function() {
    return {
      menu: false,
      menumeeting: false,
      show: false,
      status: ["เปิดให้บริการ", "ปิดปรับปรุง"]
    };
  },

  methods: {
    addTypeData: function() {
      this.menu = false;
      var new_type = document.getElementById("inputtype").value;
      var new_user = document.getElementById("inputuser").value;
      var new_price = document.getElementById("inputprice").value;
      var new_des = document.getElementById("inputdetail").value;

      if (localStorage.getItem("roomtypedata") == null) {
        localStorage.setItem("roomtypedata", "{}");
      }

      var old_type = JSON.parse(localStorage.getItem("roomtypedata"));

      old_type[new_type] = [new_user, new_price, new_des];

      localStorage.setItem("roomtypedata", JSON.stringify(old_type));
    },

    roomTypeDetail: function() {
      var type = JSON.parse(localStorage.getItem("roomtypedata"));

      if (type != null) {
        return type;
      } else {
        return {};
      }
    },

    deleteRoomType: function(roomtodel) {
      var typetodel = JSON.parse(localStorage.getItem("roomtypedata"));

      delete typetodel[roomtodel];
      localStorage.setItem("roomtypedata", JSON.stringify(typetodel));

      this.$forceUpdate();
    },

    getRoomtype: function() {
      var room = JSON.parse(localStorage.getItem("roomtypedata"));
      var type = Object.keys(room);

      if (type != null) {
        return type;
      } else {
        return [];
      }
    },

    addroom: function() {
      var new_name = document.getElementById("inputname").value;

      if (localStorage.getItem("roomnamedata") == null) {
        localStorage.setItem("roomnamedata", "{}");
      }

      var old_name = JSON.parse(localStorage.getItem("roomnamedata"));
      old_name[new_name] = [];
      localStorage.setItem("roomnamedata", JSON.stringify(old_name));

      this.menumeeting = false;
    },

    allroomname: function() {
      var name = JSON.parse(localStorage.getItem("roomnamedata"));
      if (name != null) {
        return name;
      } else {
        return [];
      }
    },

    setRoomType: function(value, key) {
      var room = JSON.parse(localStorage.getItem("roomnamedata"));
      room[key][0] = value;
      localStorage.setItem("roomnamedata", JSON.stringify(room));
    },

    setRoomStatus: function(value, key) {
      var room = JSON.parse(localStorage.getItem("roomnamedata"));
      room[key][1] = value;
      localStorage.setItem("roomnamedata", JSON.stringify(room));
    }
  }
};
</script>

<style></style>
