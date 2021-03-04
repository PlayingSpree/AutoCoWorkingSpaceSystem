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
        <v-dialog v-model="dialog" max-width="1000px">
          <v-card>
            <v-container>
              <v-card-title>
                ข้อมูลผู้ใช้
              </v-card-title>
              <v-card outlined>
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
                              v-model="profileItem.name"
                              label="ชื่อ-สกุล"
                            ></v-text-field>
                          </v-card-text>
                        </v-row>
                        <v-row>
                          <v-card-text>
                            <v-text-field
                              v-model="profileItem.email"
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
                              v-model="menupackage1"
                              :close-on-content-click="false"
                              :nudge-right="0"
                              transition="scale-transition"
                              offset-y
                              min-width="auto"
                            >
                              <template v-slot:activator="{ on, attrs }">
                                <v-text-field
                                  v-model="datepackage1"
                                  prepend-icon="mdi-calendar"
                                  readonly
                                  v-bind="attrs"
                                  v-on="on"
                                  max-width="10px"
                                ></v-text-field>
                              </template>
                              <v-date-picker
                                v-model="datepackage1"
                                @input="menupackage1 = false"
                              ></v-date-picker> </v-menu
                          ></v-col>
                          <v-col cols="2">
                            <v-card-text>
                              ถึง
                            </v-card-text>
                          </v-col>
                          <v-col cols="4"
                            ><v-menu
                              v-model="menupackage2"
                              :close-on-content-click="false"
                              :nudge-right="0"
                              transition="scale-transition"
                              offset-y
                              min-width="auto"
                            >
                              <template v-slot:activator="{ on, attrs }">
                                <v-text-field
                                  v-model="datepackage2"
                                  prepend-icon="mdi-calendar"
                                  readonly
                                  v-bind="attrs"
                                  v-on="on"
                                ></v-text-field>
                              </template>
                              <v-date-picker
                                v-model="datepackage2"
                                @input="menupackage2 = false"
                              ></v-date-picker> </v-menu
                          ></v-col>
                        </v-row>
                        <v-card-text>
                          ประเภทแพ็คเกจ
                        </v-card-text>
                        <v-card-text>
                          <v-select :items="packagedata" solo></v-select>
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
                <v-container> </v-container>
              </v-card>

              <v-card-actions>
                <v-spacer></v-spacer>
                <v-btn color="blue darken-1" text @click="close">
                  Close
                </v-btn>
              </v-card-actions>
            </v-container>
          </v-card>
        </v-dialog>
      </template>

      <template v-slot:[`item.name`]="{ item }">
        <v-card-text @click="seeProfile(item)" class="row-pointer">{{
          item.name
        }}</v-card-text>
      </template>
    </v-data-table>
  </v-card>
</template>

<script>
export default {
  data: function() {
    return {
      packagedata: ["1", "2"],
      room: ["1", "2"],
      datepackage1: new Date().toISOString().substr(0, 10),
      datepackage2: new Date().toISOString().substr(0, 10),
      menupackage1: false,
      menupackage2: false,
      dateroom: new Date().toISOString().substr(0, 10),
      menuroom: false,
      modal: false,
      search: "",
      dialog: false,
      profileIndex: -1,
      profileItem: {
        id: "",
        name: "",
        email: "",
        phone: "",
        sex: ""
      },
      defaultItem: {
        id: "",
        name: "",
        email: "",
        phone: "",
        sex: ""
      },
      headers: [
        {
          text: "รหัส",
          align: "start",
          filterable: true,
          value: "id"
        },
        { text: "ชื่อ-สกุล", value: "name" },
        { text: "email", value: "email", filterable: false },
        { text: "เบอร์โทรศัพท์", value: "phone", filterable: false }
      ],
      user: []
    };
  },
  created() {
    this.initialize();
  },

  watch: {
    dialog(val) {
      val || this.close();
    }
  },
  methods: {
    initialize: function() {
      this.user = [
        {
          id: "001",
          name: "เข็มทิศ ธัญลักษณานันท์",
          email: "example1@gmail.com",
          phone: "0892222222",
          sex: "ชาย"
        },
        {
          id: "002",
          name: "ไทธนัช เธียรประดับโชค",
          email: "example2@gmail.com",
          phone: "0892222223",
          sex: "ชาย"
        },
        {
          id: "003",
          name: "ณัชพล ศานติพิบูล",
          email: "example3@gmail.com",
          phone: "0892222224",
          sex: "ชาย"
        }
      ];
    },

    seeProfile: function(item) {
      this.profileIndex = this.user.indexOf(item);
      this.profileItem = Object.assign({}, item);
      console.log(this.dialog);
      this.dialog = true;
      console.log(this.dialog);
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
