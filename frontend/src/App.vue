<template>
  <div id="app">
    <!-- <UserProfile /> -->
    <SigninForm />
  </div>
</template>

<script>
// import UserProfile from "./components/UserProfile";
import SigninForm from "./components/SigninForm";

export default {
  name: "App",
  components: { SigninForm },
};
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  color: #2c3e50;
  min-height: 100vh;
  background-color: #f3f5fa;
  text-align: center;
}
</style>
