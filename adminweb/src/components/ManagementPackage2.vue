<template>
  <v-card class="mt-5">
    <v-container fluid>
      <v-card-title primary-title> แพ็คเกจ </v-card-title>
      <v-container class="d-flex align-content-start flex-wrap">
        <v-card
          v-for="item in packagedata"
          :key="item"
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
                {{ item.period }} วัน
              </v-card-text>
            </v-col>
          </v-row>
          <v-card-text>
            สถานะ
            <v-select
              v-model="item.status"
              :placeholder="item.status"
              :items="status"
              full-width="100px"
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
                  v-model="packageItem.period"
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
        period: "",
        status: "ปิดการใช้งาน"
      },
      defaultItem: {
        name: "",
        detail: "",
        price: "",
        period: "",
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
    showpackagedata: function() {
      var packagedata = JSON.parse(localStorage.getItem("packagedata"));

      if (packagedata != null) {
        this.packagedata = packagedata;
      } else {
        return [];
      }
    },

    setpackagestatus: function(status, item) {
      var packagedata = JSON.parse(localStorage.getItem("packagedata"));
      this.packageIndex = this.packagedata.indexOf(item);
      packagedata[this.packageIndex].status = status;
      localStorage.setItem("packagedata", JSON.stringify(packagedata));
      this.close();
      this.showpackagedata();
    },

    editItem: function(item) {
      this.packageIndex = this.packagedata.indexOf(item);
      this.packageItem = Object.assign({}, item);
      this.dialog = true;
    },

    deleteItem: function(item) {
      var packagedata = JSON.parse(localStorage.getItem("packagedata"));
      this.packageIndex = this.packagedata.indexOf(item);
      this.packageItem = Object.assign({}, item);
      packagedata.splice(this.packageIndex, 1);
      localStorage.setItem("packagedata", JSON.stringify(packagedata));
      this.$nextTick(() => {
        this.packageItem = Object.assign({}, this.defaultItem);
        this.packageIndex = -1;
      });
      this.showpackagedata();
    },

    save: function() {
      if (localStorage.getItem("packagedata") == null) {
        localStorage.setItem("packagedata", "[]");
      }

      var old_name = JSON.parse(localStorage.getItem("packagedata"));

      if (this.packageIndex > -1) {
        Object.assign(old_name[this.packageIndex], this.packageItem);
      } else {
        old_name.push(this.packageItem);
      }

      localStorage.setItem("packagedata", JSON.stringify(old_name));
      this.showpackagedata();
      this.close();
    },

    close() {
      this.dialog = false;
      this.$nextTick(() => {
        this.packageItem = Object.assign({}, this.defaultItem);
        this.packageIndex = -1;
      });
    }
  }
};
</script>
