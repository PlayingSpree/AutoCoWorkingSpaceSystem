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
                Add User
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
                                  v =>
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
                            เลือกวันที่เริ่มใช้แพ็คเกจ
                          </v-card-text>
                          <v-row class="px-2">
                            <v-col cols="4"
                              ><v-menu
                                v-model="menuprofile1"
                                :close-on-content-click="false"
                                :nudge-right="0"
                                transition="scale-transition"
                                offset-y
                                min-width="auto"
                              >
                                <template v-slot:activator="{ on, attrs }">
                                  <v-text-field
                                    v-model="dateprofile1"
                                    prepend-icon="mdi-calendar"
                                    readonly
                                    v-bind="attrs"
                                    v-on="on"
                                    max-width="10px"
                                  ></v-text-field>
                                </template>
                                <v-date-picker
                                  v-model="dateprofile1"
                                  @input="menuprofile1 = false"
                                ></v-date-picker> </v-menu
                            ></v-col>
                            <v-col cols="2">
                              <v-card-text>
                                ถึง
                              </v-card-text>
                            </v-col>
                            <v-col cols="4"
                              ><v-menu
                                v-model="menuprofile2"
                                :close-on-content-click="false"
                                :nudge-right="0"
                                transition="scale-transition"
                                offset-y
                                min-width="auto"
                              >
                                <template v-slot:activator="{ on, attrs }">
                                  <v-text-field
                                    v-model="dateprofile2"
                                    prepend-icon="mdi-calendar"
                                    readonly
                                    v-bind="attrs"
                                    v-on="on"
                                  ></v-text-field>
                                </template>
                                <v-date-picker
                                  v-model="dateprofile2"
                                  @input="menuprofile2 = false"
                                ></v-date-picker> </v-menu
                            ></v-col>
                          </v-row>
                          <v-card-text>
                            ประเภทแพ็คเกจ
                          </v-card-text>
                          <v-card-text>
                            <v-select :items="profiledata" solo></v-select>
                          </v-card-text>
                        </v-container>
                        <v-divider> </v-divider>
                        <v-container>
                          <v-card-title primary-title>
                            ห้องประชุม
                          </v-card-title>

                          <v-row>
                            <v-col no-gutters>
                              <v-card-text>
                                <v-select
                                  :items="room"
                                  label="ห้อง"
                                  class="pa-0"
                                ></v-select>
                              </v-card-text>
                            </v-col>
                            <v-col no-gutters>
                              <v-menu
                                v-model="menuroom"
                                :close-on-content-click="false"
                                transition="scale-transition"
                                offset-y
                                min-width="auto"
                                class="pa-0"
                              >
                                <template v-slot:activator="{ on, attrs }">
                                  <v-text-field
                                    v-model="dateroom"
                                    label="จองวันที่"
                                    prepend-icon="mdi-calendar"
                                    readonly
                                    v-bind="attrs"
                                    v-on="on"
                                  ></v-text-field>
                                </template>
                                <v-date-picker
                                  v-model="dateroom"
                                  @input="menuroom = false"
                                ></v-date-picker>
                              </v-menu>
                            </v-col>
                          </v-row>
                          <v-card-text>
                            ระยะเวลา
                          </v-card-text>
                          <v-row>
                            <v-col no-gutters cols="3">
                              <v-card-text>
                                <v-select class="pa-0"></v-select>
                              </v-card-text>
                            </v-col>
                            <v-col cols="2"
                              ><v-card-text>
                                ถึง
                              </v-card-text></v-col
                            >
                            <v-col no-gutters cols="3">
                              <v-card-text>
                                <v-select class="pa-0"></v-select>
                              </v-card-text>
                            </v-col>
                            <v-col> <v-card-text>น.</v-card-text></v-col>
                          </v-row>
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
                        <v-data-table :headers="headersprofile" />
                      </v-card-text>
                    </v-row>
                    <v-row>
                      <v-card-title primary-title>
                        ประวัติการจองห้องประชุม
                      </v-card-title>
                      <v-card-text>
                        <v-data-table :headers="headersmeeting" />
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

export default {
  data: function() {
    return {
      emailRules: [
        v =>
          /^\w+([.-]?\w+)*@\w+([.-]?\w+)*(\.\w{2,3})+$/.test(v) ||
          "E-mail must be valid"
      ],
      formHasErrors: false,
      profiledata: ["1", "2"],
      room: ["1", "2"],
      dateprofile1: new Date().toISOString().substr(0, 10),
      dateprofile2: new Date().toISOString().substr(0, 10),
      menuprofile1: false,
      menuprofile2: false,
      dateroom: new Date().toISOString().substr(0, 10),
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
      headersprofile: [
        {
          text: "ประเภทแพ็คเกจ",
          align: "start",
          value: "profile"
        },
        {
          text: "ระยะเวลา",
          value: "time"
        },
        {
          text: "ลบ/ยกเลิกการจอง",
          value: "reserve"
        }
      ],
      headersmeeting: [
        { text: "ครั้งที่", align: "start", value: "round" },
        {
          text: "ห้อง",
          value: "room"
        },
        {
          text: "จองวันที่",
          value: "date"
        },
        { text: "ระยะเวลา", value: "time" },
        {
          text: "สถานะ",
          value: "status"
        },
        { text: "ลบ/ยกเลิกการจอง", value: "reserve" }
      ],
      user: []
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

    seeProfile: function(item) {
      this.profileIndex = this.user.indexOf(item);
      this.profileItem = Object.assign({}, item);
      this.dialog = true;
    },

    deleteItem(item) {
      this.profileIndex = this.user.indexOf(item);
      item.is_active = false;
      this.profileItem = Object.assign({}, item);
      this.dialogDelete = true;
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
      this.formHasErrors = false;

      Object.keys(this.profileItem).forEach(f => {
        if (!this.profileItem[f]) this.formHasErrors = true;

        this.$refs[f].validate(true);
      });

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
