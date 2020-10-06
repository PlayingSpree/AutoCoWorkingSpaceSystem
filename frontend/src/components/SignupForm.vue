<template>
  <div>
    <h1>Register</h1>
    <div class="sign-up-form">
      <div class="container">
        <div class="sign-up-form__row">
          <div class="h-100 d-flex justify-content-center align-items-center">
            <div class="col-md-8 rounded px-5 py-4 shadow bg-white text-left">
              <form id="signup-form" v-on:submit.prevent="submit">
                <div class="row">
                  <div class="col-12 form-group">
                    <label class="col-form-label col-form-label-lg"
                      >Email <span class="text-danger">*</span></label
                    >
                    <input
                      type="email"
                      v-model.trim="email"
                      class="form-control form-control-lg"
                    />
                  </div>

                  <div class="col-12 form-group">
                    <label class="col-form-label col-form-label-lg"
                      >Password <span class="text-danger">*</span></label
                    >
                    <input
                      type="password"
                      v-model.trim="password"
                      class="form-control form-control-lg"
                    />
                  </div>

                  <div class="col-12 form-group">
                    <label class="col-form-label col-form-label-lg"
                      >Confirm Password
                      <span class="text-danger">*</span></label
                    >
                    <input
                      type="password"
                      v-model.trim="confirmPassword"
                      class="form-control form-control-lg"
                    />
                  </div>

                  <div class="col-12 form-group text-center">
                    <button class="btn submit-btn btn-lg col-4">Sign Up</button>
                  </div>
                </div>
              </form>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
<script>
import {
  required,
  email,
  minLength,
  maxLength,
} from "vuelidate/lib/validators";

export default {
  name: "SignupForm",
  data: function () {
    return {
      email: "",
      password: "",
      confirmPassword: "",
    };
  },

  validations: {
    fullname: { required },
    email: { required, email },
    country: { required },
    password: { required, minLength: minLength(8), maxLength: maxLength(20) },
  },

  methods: {
    validationStatus: function (validation) {
      return typeof validation != "undefined" ? validation.$error : false;
    },

    submit: function () {
      this.$v.$touch();
      if (this.$v.$pendding || this.$v.$error) return;

      alert("Data Submit");
    },
  },
};
</script>
<style>
.sign-up-form {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  color: #2c3e50;
}

.container {
  margin: 0 auto;
}

.submit-btn {
  background: #ebb729;
  color: #ffffff;
  font-weight: bold;
}
</style>