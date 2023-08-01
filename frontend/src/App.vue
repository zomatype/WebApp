<template>
  <div id="app">
    <AppHeader/>
    <Home/>
    <AppFooter/>
  </div>
</template>

<script>
import AppHeader from './components/modules/AppHeader'
import AppFooter from './components/modules/AppFooter.vue'
import Home from './components/pages/TopPage.vue'

export default {
  name: 'App',
  components: {
    Home,
    AppHeader,
    AppFooter,
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
