<template>
  <v-card>
    <v-container fluid>
      <v-row
        ><v-card-title primary-title>
          ประเภทห้องประชุม
        </v-card-title></v-row
      >

      <v-row>
        <v-container fluid>
          <v-row>
            <v-col v-for="item in roomdetail()" :key="item[0]" :id="item[0]" cols="2">
              <v-card outlined>
                <v-responsive :aspect-ratio="1 / 1">
                  <v-container fluid>
                    <v-row>
                      <v-col cols="12"
                        ><v-card-title class="justify-center">
                          {{ item[0] }}
                        </v-card-title>
                        <v-card-text>
                          จำนวนคนสูงสุด: {{ item[1] }}
                        </v-card-text>
                        <v-card-text>
                          ราคา: {{ item[2] }} ฿/hr
                        </v-card-text></v-col
                      >
                    </v-row>
                    <v-row class="justify-center">
                      <v-col cols="6">
                        <v-card-actions>
                          <v-btn icon
                            ><v-icon style="color: #9CCC65"
                              >mdi-pencil</v-icon
                            ></v-btn
                          >
                          <v-btn @click="deleteroomdetail(item[0], item[1], item[2])" icon
                            ><v-icon style="color: #B71C1C"
                              >mdi-delete</v-icon
                            ></v-btn
                          >
                        </v-card-actions>
                      </v-col>
                    </v-row>
                  </v-container>
                </v-responsive>
              </v-card>
            </v-col>
            <v-col cols="2">
              <v-card outlined>
                <v-responsive :aspect-ratio="1 / 1">
                  <v-menu
                    v-model="menu"
                    :close-on-content-click="false"
                    :nudge-width="100"
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
                            <v-overflow-btn
                              class="my-2"
                              :items="roomSize"
                              id="inputsize"
                              label="ขนาดห้อง"
                              editable
                            ></v-overflow-btn>
                          </v-list-item-action>
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
                        <v-btn color="primary" text @click="addData">
                          OK
                        </v-btn>
                      </v-card-actions>
                    </v-card>
                  </v-menu>
                </v-responsive>
              </v-card>
            </v-col>
          </v-row>
        </v-container>
      </v-row>
    </v-container>
  </v-card>
</template>

<script>
export default {
  data: function() {
    return {
      roomSize: ["ห้องเล็ก", "ห้องกลาง", "ห้องใหญ่"],
      menu: false
    };
  },

  methods: {
    addData: function() {
      this.menu = false;
      var new_size = document.getElementById("inputsize").value;
      var new_user = document.getElementById("inputuser").value;
      var new_price = document.getElementById("inputprice").value;

      if (localStorage.getItem("roomsizedata") == null) {
        localStorage.setItem("roomsizedata", "[]");
      }
      if (localStorage.getItem("roomuserdata") == null) {
        localStorage.setItem("roomuserdata", "[]");
      }
      if (localStorage.getItem("roompricedata") == null) {
        localStorage.setItem("roompricedata", "[]");
      }

      var old_size = JSON.parse(localStorage.getItem("roomsizedata"));
      old_size.push(new_size);
      localStorage.setItem("roomsizedata", JSON.stringify(old_size));

      var old_user = JSON.parse(localStorage.getItem("roomuserdata"));
      old_user.push(new_user);
      localStorage.setItem("roomuserdata", JSON.stringify(old_user));

      var old_price = JSON.parse(localStorage.getItem("roompricedata"));
      old_price.push(new_price);
      localStorage.setItem("roompricedata", JSON.stringify(old_price));
    },

    roomdetail: function() {
      var detail = [];
      var size = JSON.parse(localStorage.getItem("roomsizedata"));
      var user = JSON.parse(localStorage.getItem("roomuserdata"));
      var price = JSON.parse(localStorage.getItem("roompricedata"));

      if (size != null) {
        for (var i = 0; i < size.length; i++) {
          detail.push([size[i], user[i], price[i]]);
        }
        return detail;
      } else {
        return [];
      }
    },

    deleteroomdetail: function(sizetodel, usertodel, pricetodel) {
      var size = sizetodel
      var user = usertodel
      var price = pricetodel
      

      console.log(size)
      console.log(user)
      console.log(price)

      console.log(this.roomdetail())

      for(var i=0; i<this.roomdetail().length; i++){
        if(size == this.roomdetail()[i][0] & user == this.roomdetail()[i][1] & price == this.roomdetail()[i][2]){
          var old_size = JSON.parse(localStorage.getItem("roomsizedata"));
          old_size.splice(i, 1)
          localStorage.setItem("roomsizedata", JSON.stringify(old_size));
          var old_user = JSON.parse(localStorage.getItem("roomuserdata"));
          old_user.splice(i, 1)
          localStorage.setItem("roomuserdata", JSON.stringify(old_user));
          var old_price = JSON.parse(localStorage.getItem("roompricedata"));
          old_price.splice(i, 1)
          localStorage.setItem("roompricedata", JSON.stringify(old_price));
        }
      }

      // localStorage.setItem("roomsizedata", '[]');
      // localStorage.setItem("roomuserdata", '[]');
      // localStorage.setItem("roompricedata", '[]');
      this.$forceUpdate();
    }
  }
};
</script>

<style></style>
