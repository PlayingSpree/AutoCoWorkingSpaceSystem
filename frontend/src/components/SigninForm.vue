<template>
  <div>
    <h1>Sign in</h1>

    <div class="sign-in-form">
      <div class="container">
        <div class="sign-up-form__row">
          <div class="h-100 d-flex justify-content-center align-items-center">
            <div class="col-md-8 rounded px-5 py-4 shadow bg-white text-left">
              <Form @submit="onSubmit">
                <div class="row">
                  <div class="col-12 form-group">
                    <label class="col-form-label col-form-label-lg">
                      Email
                      <span class="text-danger">*</span>
                    </label>
                    <Field
                      name="email"
                      as="input"
                      type="email"
                      :rules="validateEmail"
                      class="form-control form-control-lg"
                    />
                    <ErrorMessage name="email" />
                  </div>

                  <div class="col-12 form-group">
                    <label class="col-form-label col-form-label-lg">
                      Password
                      <span class="text-danger">*</span>
                    </label>
                    <Field
                      name="password"
                      as="input"
                      type="password"
                      :rules="validatePassword"
                      v-on:keyup="tpassword"
                      class="form-control form-control-lg"
                    />
                    <ErrorMessage name="password" />
                  </div>

                  <div class="col-12 form-group text-center">
                    <button class="btn submit-btn btn-lg col-4">Sign Up</button>
                  </div>
                </div>
              </Form>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
<script>
import { Form, Field, ErrorMessage } from "vee-validate";

export default {
  components: {
    Form,
    Field,
    ErrorMessage
  },
  name: "SigninForm",

  methods: {
    onSubmit(values) {
      alert(JSON.stringify(values, null, 2));
    },

    confimPassword: function(e) {
      this.confirmpassword = e.target.value;
    },

    tpassword: function(e) {
      this.password = e.target.value;
    },

    validateEmail(value) {
      // if the field is empty
      if (!value) {
        return "This field is required";
      }

      // if the field is not a valid email
      if (!/^[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,4}$/i.test(value)) {
        return "This field must be a valid email";
      }

      // All is good
      return true;
    },

    validatePassword(value) {
      var regularExpression = /^(?=.*[0-9])(?=.*[A-Z]).{8,20}$/;
      // if the field is empty
      if (!value) {
        return "This field is required";
      }

      // if the field is not a valid password by RE.
      if (!regularExpression.test(value)) {
        return "Password must be at least 8 characters, minimum of 1 numeric, and 1 upper case letter.";
      }
      // All is good
      return true;
    }
  }
};
</script>
<style>
.sign-in-form {
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
