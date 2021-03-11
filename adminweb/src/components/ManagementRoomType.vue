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
          <v-card-title primary-title>
            {{ item.name }} <v-spacer></v-spacer>
            <v-tooltip bottom class="ml-3">
              <template v-slot:activator="{ on, attrs }">
                <v-icon v-bind="attrs" v-on="on" small>mdi-information</v-icon>
              </template>
              <span>{{ item.detail }}</span>
            </v-tooltip>
          </v-card-title>
          <v-card-text> จำนวนคนสูงสุด: {{ item.numUser }} </v-card-text>
          <v-card-text> ราคา: {{ item.price }} ฿/hr </v-card-text>
          <v-card-actions class="justify-center">
            <v-btn @click="editItem(item)" icon
              ><v-icon style="color: #9CCC65">mdi-pencil</v-icon></v-btn
            >
            <v-btn @click="deleteItem(item)" icon
              ><v-icon style="color: #B71C1C">mdi-delete</v-icon></v-btn
            >
          </v-card-actions>
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
                  v-model="roomtypeItem.numUser"
                  label="จำนวนคนสูงสุด"
                  suffix="คน"
                  type="number"
                  required
                ></v-text-field>
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
export default {
  data: function() {
    return {
      dialog: false,
      roomtypeIndex: -1,
      roomtypedata: [],
      roomtypeItem: {
        name: "",
        detail: "",
        numUser: "",
        price: ""
      },
      defaultItem: {
        name: "",
        detail: "",
        numUser: "",
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
    showroomtypedata: function() {
      var roomtypedata = JSON.parse(localStorage.getItem("roomtypedata"));

      if (roomtypedata != null) {
        this.roomtypedata = roomtypedata;
      } else {
        return [];
      }
    },

    editItem: function(item) {
      this.roomtypeIndex = this.roomtypedata.indexOf(item);
      this.roomtypeItem = Object.assign({}, item);
      this.dialog = true;
    },

    deleteItem: function(item) {
      var roomtypedata = JSON.parse(localStorage.getItem("roomtypedata"));
      this.roomtypeIndex = this.roomtypedata.indexOf(item);
      this.roomtypeItem = Object.assign({}, item);
      roomtypedata.splice(this.roomtypeIndex, 1);
      localStorage.setItem("roomtypedata", JSON.stringify(roomtypedata));
      this.$nextTick(() => {
        this.roomtypeItem = Object.assign({}, this.defaultItem);
        this.roomtypeIndex = -1;
      });
      this.showroomtypedata();
    },

    save: function() {
      if (localStorage.getItem("roomtypedata") == null) {
        localStorage.setItem("roomtypedata", "[]");
      }

      var old_name = JSON.parse(localStorage.getItem("roomtypedata"));

      if (this.roomtypeIndex > -1) {
        Object.assign(old_name[this.roomtypeIndex], this.roomtypeItem);
      } else {
        old_name.push(this.roomtypeItem);
      }

      localStorage.setItem("roomtypedata", JSON.stringify(old_name));
      this.showroomtypedata();
      this.close();
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
