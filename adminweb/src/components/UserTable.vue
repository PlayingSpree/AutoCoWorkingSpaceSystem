<template>
  <v-card class="mt-5">
    <v-card-title primary-title>
      ผู้ใช้
    </v-card-title>
    <v-card-title>
      <v-text-field
        v-model="search"
        append-icon="mdi-magnify"
        label="Search"
        single-line
        hide-details
      ></v-text-field>
    </v-card-title>
    <v-data-table
      :headers="headers"
      :items="user"
      item-key="id"
      :search="search"
    >
      <template v-slot:top>
        <v-toolbar flat>
          <v-spacer></v-spacer>
          <v-dialog v-model="dialog" max-width="1000px">
            <template v-slot:activator="{ on, attrs }">
              <v-btn color="primary" dark class="mb-2" v-bind="attrs" v-on="on">
                เพิ่มผู้ใช้
              </v-btn>
            </template>
            <v-card>
              <v-container>
                <v-card-title>
                  ข้อมูลผู้ใช้
                </v-card-title>
                <v-card outlined ref="form">
                  <v-container>
                    <v-row>
                      <v-col>
                        <v-container>
                          <v-row>
                            <v-card-title>
                              รหัส {{ profileItem.id }}
                            </v-card-title>
                          </v-row>
                          <v-row>
                            <v-card-text>
                              <v-text-field
                                :ref="profileItem.name"
                                v-model="profileItem.name"
                                :rules="[
                                  () =>
                                    !!profileItem.name ||
                                    'This field is required'
                                ]"
                                label="ชื่อ-สกุล"
                              ></v-text-field>
                            </v-card-text>
                          </v-row>
                          <v-row>
                            <v-card-text>
                              <v-text-field
                                :ref="profileItem.email"
                                v-model="profileItem.email"
                                :rules="[
                                  () =>
                                    !!profileItem.email ||
                                    'This field is required',
                                  (v) =>
                                    /^\w+([.-]?\w+)*@\w+([.-]?\w+)*(\.\w{2,3})+$/.test(
                                      v
                                    ) || 'E-mail must be valid'
                                ]"
                                label="email"
                              ></v-text-field>
                            </v-card-text>
                          </v-row>
                          <v-row>
                            <v-card-text>
                              <v-text-field
                                v-model="profileItem.phone"
                                label="เบอร์โทรศัพท์"
                              ></v-text-field>
                            </v-card-text>
                          </v-row>
                        </v-container>
                      </v-col>
                      <v-divider vertical></v-divider>
                      <v-col>
                        <v-container>
                          <v-card-title primary-title>
                            แพ็คเกจ
                          </v-card-title>
                          <v-card-text>
                            <span>เลือกวันที่เริ่มใช้แพ็คเกจ</span>
                            <date-picker
                              v-model="datesub"
                              lang="en"
                              type="date"
                              confirm
                              :time-picker-options="{
                                start: '00:00',
                                step: '01:00',
                                end: '23:00',
                                format: 'HH:mm'
                              }"
                              range
                            ></date-picker>
                          </v-card-text>
                          <v-card-text>
                            <span>ประเภทแพ็คเกจ</span>
                            <v-select
                              v-model="coworkpackage"
                              :items="allpack"
                              label="ประเภทของแพ็คเกจ"
                              @input="choosepackage(coworkpackage)"
                              solo
                            ></v-select>
                          </v-card-text>
                          <v-card-actions
                            ><v-spacer></v-spacer
                            ><v-btn color="primary" @click="confirmsub()"
                              >บันทึก</v-btn
                            ></v-card-actions
                          >
                        </v-container>
                        <v-divider> </v-divider>
                        <v-container>
                          <v-card-title primary-title>
                            ห้องประชุม
                          </v-card-title>
                          <v-card-text>
                            <span>เลือกวันที่และเวลา</span>
                            <date-picker
                              v-model="dateroom"
                              lang="en"
                              type="datetime"
                              :time-picker-options="{
                                start: '00:00',
                                step: '01:00',
                                end: '23:00',
                                format: 'HH:mm'
                              }"
                              confirm
                              range
                            ></date-picker>
                          </v-card-text>
                          <v-card-text>
                            <span>เลือกห้องประชุม</span>
                            <v-select
                              v-model="room"
                              :items="allroom"
                              label="ห้อง"
                              @input="chooseroom(room)"
                              solo
                            ></v-select>
                          </v-card-text>
                          <v-card-actions>
                            <v-spacer></v-spacer
                            ><v-btn color="primary" @click="confirmbook()"
                              >บันทึก</v-btn
                            >
                          </v-card-actions>
                        </v-container>
                      </v-col>
                    </v-row>
                  </v-container>
                </v-card>

                <v-card outlined class="mt-2">
                  <v-container>
                    <v-row>
                      <v-card-title primary-title>
                        ประวัติการซื้อแพ็คเกจ
                      </v-card-title>
                      <v-card-text>
                        <v-data-table
                          :headers="headerssub"
                          :items="subhistory"
                        />
                      </v-card-text>
                    </v-row>
                    <v-row>
                      <v-card-title primary-title>
                        ประวัติการจองห้องประชุม
                      </v-card-title>
                      <v-card-text>
                        <v-data-table
                          :headers="headersmeeting"
                          :items="meetinghistory"
                        />
                      </v-card-text>
                    </v-row>
                  </v-container>
                </v-card>

                <v-card-actions>
                  <v-spacer></v-spacer>
                  <v-btn color="blue darken-1" text @click="close">
                    Close
                  </v-btn>
                  <v-btn text @click="save">
                    Save
                  </v-btn>
                </v-card-actions>
              </v-container>
            </v-card>
          </v-dialog>
          <v-dialog v-model="dialogDelete" max-width="500px">
            <v-card>
              <v-card-title class="headline"
                >Are you sure you want to delete this item?</v-card-title
              >
              <v-card-actions>
                <v-spacer></v-spacer>
                <v-btn color="blue darken-1" text @click="closeDelete"
                  >Cancel</v-btn
                >
                <v-btn color="blue darken-1" text @click="deleteItemConfirm"
                  >OK</v-btn
                >
                <v-spacer></v-spacer>
              </v-card-actions>
            </v-card>
          </v-dialog>
        </v-toolbar>
      </template>

      <template v-slot:[`item.name`]="{ item }">
        <v-card-text @click="seeProfile(item)" class="row-pointer">{{
          item.name
        }}</v-card-text>
      </template>
      <template class="justify-center" v-slot:[`item.actions`]="{ item }">
        <v-icon small @click="deleteItem(item)">
          mdi-delete
        </v-icon>
      </template>
    </v-data-table>
  </v-card>
</template>

<script>
import axios from "axios";
import DatePicker from "vue2-datepicker";
import "vue2-datepicker/index.css";

export default {
  components: {
    DatePicker
  },
  data: function() {
    return {
      emailRules: [
        (v) =>
          /^\w+([.-]?\w+)*@\w+([.-]?\w+)*(\.\w{2,3})+$/.test(v) ||
          "E-mail must be valid"
      ],
      formHasErrors: false,
      datesub: [new Date(), new Date()],
      menuprofile1: false,
      menuprofile2: false,
      dateroom: [new Date(), new Date()],
      menuroom: false,
      modal: false,
      search: "",
      dialog: false,
      dialogDelete: false,
      profileIndex: -1,
      profileItem: {
        id: "",
        first_name: "",
        last_name: "",
        name: "",
        email: "",
        phone: "",
        is_active: true
      },
      defaultItem: {
        id: "",
        first_name: "",
        last_name: "",
        name: "",
        email: "",
        phone: "",
        is_active: true
      },
      headers: [
        {
          text: "รหัส",
          align: "start",
          filterable: true,
          value: "id"
        },
        { text: "ชื่อ-สกุล", value: "name" },
        { text: "email", value: "email" },
        { text: "เบอร์โทรศัพท์", value: "phone", filterable: false },
        { text: "การจัดการ", value: "actions", sortable: false }
      ],
      headerssub: [
        {
          text: "ประเภทแพ็คเกจ",
          align: "start",
          value: "package"
        },
        {
          text: "ระยะเวลา",
          value: "time"
        }
      ],
      headersmeeting: [
        {
          text: "ครั้งที่",
          value: "index"
        },
        {
          text: "ห้อง",
          value: "room"
        },
        { text: "วันที่", value: "date" },
        { text: "ระยะเวลา", value: "time" }
      ],
      user: [],
      subhistory: [],
      meetinghistory: [],
      coworkpackage: [],
      room: [],
      datatosub: {},
      datatobook: {},
      allroom: [],
      allpack: []
    };
  },
  created() {
    this.getUser();
  },

  watch: {
    dialog(val) {
      val || this.close();
    }
  },
  methods: {
    async getUser() {
      let user = await axios.get("auth/admin/user/");
      let activeuser = [];
      let newuser = user.data;
      for (let i = 0; i < newuser.length; i++) {
        newuser[i].name = newuser[i].first_name + " " + newuser[i].last_name;
        if (newuser[i].is_active == true) {
          activeuser.push(newuser[i]);
        }
      }

      this.user = activeuser;
    },

    async getsub(id) {
      let sub = await axios.get(`coworkingspace/subscription/?user=${id}`);
      sub = sub.data;
      let subhistory = [];

      let eachsub = {
        package: "",
        time: "",
        reserve: ""
      };

      for (let i = 0; i < sub.length; i++) {
        eachsub.package = sub[i].package.name;
        eachsub.time =
          new Date(sub[i].date_start) + " - " + new Date(sub[i].date_end);
        subhistory.push(eachsub);
      }

      this.subhistory = subhistory;
    },

    async getmeet(id) {
      let meet = await axios.get(`meetingroom/booking/?user=${id}`);
      meet = meet.data;
      let meethistory = [];
      let eachmeet = {
        index: "",
        room: "",
        time: ""
      };
      for (let i = 0; i < meet.length; i++) {
        eachmeet = {};
        eachmeet.index = i + 1;
        eachmeet.room = meet[i].room.name;
        eachmeet.date = new Date(meet[i].date_start);
        eachmeet.time =
          (new Date(meet[i].date_end).getDay() -
            new Date(meet[i].date_start).getDay()) *
            24 +
          (new Date(meet[i].date_end).getHours() -
            new Date(meet[i].date_start).getHours()) +
          " ชม.";
        meethistory.push(eachmeet);
      }

      this.meetinghistory = meethistory;
    },

    seeProfile: function(item) {
      this.coworkpackage = [];
      this.profileIndex = this.user.indexOf(item);
      this.profileItem = Object.assign({}, item);
      this.getsub(this.profileItem.id);
      this.getmeet(this.profileItem.id);
      this.getcoworkpackage();
      this.getmeetingroom();
      this.dialog = true;
    },

    deleteItem(item) {
      this.profileIndex = this.user.indexOf(item);
      item.is_active = false;
      this.profileItem = Object.assign({}, item);
      this.dialogDelete = true;
    },

    async getcoworkpackage() {
      let allpackage = await axios.get("coworkingspace/package/");
      allpackage = allpackage.data;
      for (let i = 0; i < allpackage.length; i++) {
        this.allpack.push(allpackage[i].name);
      }
    },

    async getmeetingroom() {
      let allroom = await axios.get("meetingroom/");
      allroom = allroom.data;
      for (let i = 0; i < allroom.length; i++) {
        this.allroom.push(allroom[i].name);
      }
    },

    async choosepackage(value) {
      let allpackage = await axios.get("coworkingspace/package/");
      allpackage = allpackage.data;
      for (let i = 0; i < allpackage.length; i++) {
        if (allpackage[i].name == value) {
          let id = allpackage[i].id;
          this.datatosub.package = id;
        }
      }
    },

    async chooseroom(value) {
      let allroom = await axios.get("meetingroom/");
      allroom = allroom.data;
      for (let i = 0; i < allroom.length; i++) {
        if (allroom[i].name == value) {
          let id = allroom[i].id;
          this.datatobook.room = id;
        }
      }
    },

    async confirmsub() {
      this.datatosub.date_start = this.datesub[0].toISOString().substr(0, 10);
      this.datatosub.date_end = this.datesub[1].toISOString().substr(0, 10);
      this.datatosub.user = this.profileItem.id;
      await axios.post("coworkingspace/subscription/", this.datatosub);
      this.close();
    },

    async confirmbook() {
      this.datatobook.date_start = this.dateroom[0].toISOString();
      this.datatobook.date_end = this.dateroom[1].toISOString();
      this.datatobook.user = this.profileItem.id;
      await axios.post("meetingroom/booking/", this.datatobook);
      this.close();
    },

    async deleteItemConfirm() {
      await axios.put(
        `auth/admin/user/${this.user[this.profileIndex].id}/`,
        this.profileItem
      );
      this.closeDelete();
      this.getUser();
    },

    closeDelete() {
      this.dialogDelete = false;
      this.$nextTick(() => {
        this.profileItem = Object.assign({}, this.defaultItem);
        this.profileIndex = -1;
      });
    },

    async save() {
      this.profileItem.first_name = this.profileItem.name.split(" ")[0];
      this.profileItem.last_name = this.profileItem.name.split(" ")[1];
      this.profileItem.is_active = true;
      if (this.profileIndex > -1) {
        await axios.put(
          `auth/admin/user/${this.user[this.profileIndex].id}/`,
          this.profileItem
        );
      } else {
        await axios.post("auth/admin/user/", this.profileItem);
      }
      this.getUser();
      this.close();
    },

    close() {
      this.dialog = false;
      this.$nextTick(() => {
        this.profileItem = Object.assign({}, this.defaultItem);
        this.profileIndex = -1;
      });
    }
  }
};
</script>

<style>
.row-pointer {
  cursor: pointer;
}
</style>
