<template>
  <v-card class="mt-5">
    <v-container fluid>
      <v-card-title primary-title> แพ็คเกจ </v-card-title>
      <v-container class="d-flex align-content-start flex-wrap">
        <v-card
          v-for="key in Object.keys(packagedata())"
          :key="key"
          outlined
          width="300px"
          height="400px"
          class="mx-2"
        >
          <v-card-title class="justify-center">
            {{ key }} <v-spacer></v-spacer> <v-btn @click="deletePackageName(key)" icon
              ><v-icon style="color: #B71C1C">mdi-delete</v-icon></v-btn
            >
          </v-card-title>
          <v-card-text style="color: #ffffff"> รายละเอียด </v-card-text>
          <v-card-text style="font-size: 20px">
            {{ packagedata()[key][0] }}
          </v-card-text>
          <v-row>
            <v-col cols="6">
              <v-card-text> ราคา </v-card-text>
              <v-card-text style="color: #ffffffb3; font-size: 20px">
                {{ packagedata()[key][1] }} บาท
              </v-card-text>
            </v-col>
            <v-col cols="6">
              <v-card-text> ระยะเวลา </v-card-text>
              <v-card-text style="color: #ffffffb3; font-size: 20px">
                {{ packagedata()[key][2] }} วัน
              </v-card-text>
            </v-col>
          </v-row>
          <v-card-text> สถานะ </v-card-text>
          <v-card-text>
            <v-select
              v-model="selectstatus"
              :placeholder="packagedata()[key][3]"
              :items="status"
              full-width="100px"
              @input="setPackageStatus(selectstatus, key)"
              solo
            ></v-select>
          </v-card-text>
        </v-card>
        <v-card outlined width="300px" height="400px" class="mx-2">
          <v-menu
            v-model="menu"
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
                      label="ชื่อแพ็คเกจ"
                      v-model="packageName"
                      id="inputname"
                    ></v-text-field>
                  </v-list-item-action>
                </v-list-item>

                <v-list-item>
                  <v-list-tile-action>
                    <v-textarea
                      name="describtion"
                      label="รายละเอียด"
                      id="inputdetail"
                      outlined
                    ></v-textarea>
                  </v-list-tile-action>
                </v-list-item>

                <v-list-item>
                  <v-list-tile-title class="mr-2">ราคา :</v-list-tile-title>
                  <v-list-tile-action>
                    <v-text-field
                      v-model="packagePrice"
                      id="inputprice"
                      class="mt-0 pt-0"
                      hide-details
                      single-line
                      type="number"
                      style="width: 40px"
                    ></v-text-field>
                  </v-list-tile-action>
                  <v-list-tile-title>บาท</v-list-tile-title>
                </v-list-item>

                <v-list-item>
                  <v-list-tile-title class="mr-2">ระยะเวลา :</v-list-tile-title>
                  <v-list-tile-action>
                    <v-text-field
                      v-model="packagerange"
                      id="inputrange"
                      class="mt-0 pt-0"
                      hide-details
                      single-line
                      type="number"
                      style="width: 50px"
                    ></v-text-field>
                  </v-list-tile-action>
                  <v-list-tile-title>วัน</v-list-tile-title>
                </v-list-item>
              </v-list>

              <v-card-actions>
                <v-spacer></v-spacer>

                <v-btn text @click="menu = false"> Cancel </v-btn>
                <v-btn color="primary" text @click="addNewPackage"> OK </v-btn>
              </v-card-actions>
              
            </v-card>
          </v-menu>
        </v-card>
        
      </v-container>
    </v-container>
  </v-card>
</template>

<script>
export default {
  data: function() {
    return {
      menu: false,
      status: ["เปิดการใช้งาน", "ปิดการใช้งาน"],
      statusgroup: 0
    };
  },
  methods: {
    addNewPackage: function() {
      this.menu = false;
      var new_name = document.getElementById("inputname").value;
      var new_detail = document.getElementById("inputdetail").value;
      var new_price = document.getElementById("inputprice").value;
      var new_range = document.getElementById("inputrange").value;

      if (localStorage.getItem("packagedata") == null) {
        localStorage.setItem("packagedata", "{}");
      }

      var old_name = JSON.parse(localStorage.getItem("packagedata"));

      old_name[new_name] = [new_detail, new_price, new_range, "ปิดการใช้งาน"];

      localStorage.setItem("packagedata", JSON.stringify(old_name));
    },

    packagedata: function() {
      var packagedata = JSON.parse(localStorage.getItem("packagedata"));

      if (packagedata != null) {
        return packagedata;
      } else {
        return {};
      }
    },

    setPackageStatus: function(value, key) {
      var packagedata = JSON.parse(localStorage.getItem("packagedata"));
      packagedata[key][3] = value;
      localStorage.setItem("packagedata", JSON.stringify(packagedata));
    },

    deletePackageName: function(packagetodel) {
      var nametodel = JSON.parse(localStorage.getItem("packagedata"));

      delete nametodel[packagetodel];
      localStorage.setItem("packagedata", JSON.stringify(nametodel));

      this.$forceUpdate();
    }
  }
};
</script>
