<template>
  <div id="app">
    <Nav />
    <router-view/>
    <Footer />
  </div>
</template>

<script>
import Nav from "./components/Nav";
import Footer from "./components/Footer";
export default {
  components: {Nav, Footer}
  
}
</script>

<style>
@import "assets/css/style.css";
</style>