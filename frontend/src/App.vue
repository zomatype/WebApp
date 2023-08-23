<template>
  <div id="app">
    <Header />
    <div 
      id="nav" 
      class="tab-area-base">
      <ul class="tab-menu-base">
        <li><router-link to="/">Home</router-link></li>
        <li><router-link to="/list">Rounting Test</router-link></li>
      </ul>
    </div>
    <router-view />
    <Footer />
  </div>
</template>

<script>
import Header from './components/modules/AppHeader.vue';
import Footer from './components/modules/AppFooter.vue';

export default {
  name: "App",
  components: {
    Header,
    Footer
  },
};
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}
</style>
