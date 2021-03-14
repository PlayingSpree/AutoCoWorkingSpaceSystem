<template>
  <v-card class="mt-5">
    <v-container fluid>
      <v-card-title primary-title> แพ็คเกจ </v-card-title>
      <v-container class="d-flex align-content-start flex-wrap">
        <v-card
          v-for="item in packagedata"
          :key="'package' + item"
          outlined
          width="300px"
          height="400px"
          class="mx-2 mb-4"
        >
          <v-card-title primary-title>
            {{ item.name }} <v-spacer></v-spacer>
            <v-btn @click="editItem(item)" icon
              ><v-icon style="color: #9CCC65">mdi-pencil</v-icon></v-btn
            >
            <v-btn @click="deleteItem(item)" icon
              ><v-icon style="color: #B71C1C">mdi-delete</v-icon></v-btn
            >
          </v-card-title>
          <v-card-text style="color: #ffffff"> รายละเอียด </v-card-text>
          <v-card-text style="font-size: 20px">
            {{ item.detail }}
          </v-card-text>
          <v-row>
            <v-col cols="6">
              <v-card-text> ราคา </v-card-text>
              <v-card-text style="color: #ffffffb3; font-size: 20px">
                {{ item.price }} บาท
              </v-card-text>
            </v-col>
            <v-col cols="6">
              <v-card-text> ระยะเวลา </v-card-text>
              <v-card-text style="color: #ffffffb3; font-size: 20px">
                {{ item.duration }} วัน
              </v-card-text>
            </v-col>
          </v-row>
          <v-card-text>
            สถานะ
            <v-select
              v-model="item.status"
              :items="status"
              @input="setpackagestatus(item.status, item)"
              solo
            ></v-select
          ></v-card-text>
        </v-card>
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
                  label="ชื่อแพ็คเกจ"
                  v-model="packageItem.name"
                  required
                ></v-text-field>
              </v-card-text>
              <v-card-text>
                <v-textarea
                  v-model="packageItem.detail"
                  name="describtion"
                  label="รายละเอียด"
                  outlined
                ></v-textarea>
              </v-card-text>
              <v-card-text>
                <v-text-field
                  v-model="packageItem.price"
                  label="ราคา"
                  suffix="บาท"
                  type="number"
                  required
                ></v-text-field>
              </v-card-text>
              <v-card-text>
                <v-text-field
                  v-model="packageItem.duration"
                  label="ระยะเวลา"
                  suffix="วัน"
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
    </v-container>
  </v-card>
</template>

<script>
import axios from "axios";

export default {
  data: function() {
    return {
      status: ["เปิดการใช้งาน", "ปิดการใช้งาน"],
      dialog: false,
      packageIndex: -1,
      packagedata: [],
      packageItem: {
        name: "",
        detail: "",
        price: "",
        duration: "",
        is_active: false,
        status: "ปิดการใช้งาน"
      },
      defaultItem: {
        name: "",
        detail: "",
        price: "",
        duration: "",
        is_active: false,
        status: "ปิดการใช้งาน"
      }
    };
  },

  computed: {
    formTitle() {
      return this.packageIndex === -1 ? "New Item" : "Edit Item";
    }
  },

  watch: {
    dialog(val) {
      val || this.close();
    }
  },

  created() {
    this.showpackagedata();
  },

  methods: {
    async showpackagedata() {
      var packagedata = await axios.get("coworkingspace/package/");

      this.packagedata = packagedata.data;

      for (var i = 0; i < this.packagedata.length; i++) {
        if (this.packagedata[i].is_active == true) {
          this.packagedata[i].status = "เปิดการใช้งาน";
        } else {
          this.packagedata[i].status = "ปิดการใช้งาน";
        }
      }
    },

    editItem: function(item) {
      this.packageIndex = this.packagedata.indexOf(item);
      this.packageItem = Object.assign({}, item);
      this.dialog = true;
    },

    async deleteItem(item) {
      this.packageIndex = this.packagedata.indexOf(item);

      await axios.delete(
        `coworkingspace/package/${this.packagedata[this.packageIndex].id}/`
      );

      this.showpackagedata();
      this.close();
    },

    async save() {
      if (this.packageIndex > -1) {
        await axios.put(
          `coworkingspace/package/${this.packagedata[this.packageIndex].id}/`,
          this.packageItem
        );
      } else {
        await axios.post("coworkingspace/package/", this.packageItem);
      }
      this.showpackagedata();
      this.close();
    },

    close() {
      this.dialog = false;
      this.$nextTick(() => {
        this.packageItem = Object.assign({}, this.defaultItem);
        this.packageIndex = -1;
      });
    },

    async setpackagestatus(status, item) {
      let active = false;
      if (status == "เปิดการใช้งาน") {
        active = true;
      } else {
        active = false;
      }
      this.packageIndex = this.packagedata.indexOf(item);
      this.packageItem = Object.assign({}, item);
      this.packageItem.is_active = active;
      await axios.put(
        `coworkingspace/package/${this.packagedata[this.packageIndex].id}/`,
        this.packageItem
      );
      this.close();
      this.showpackagedata();
    }
  }
};
</script>
