<template>
  <v-app>
    <my-toolbar></my-toolbar>
    <nav-drawer></nav-drawer>
    <v-main>
      <transition name="fade">
        <router-view></router-view>
      </transition>
    </v-main>
  </v-app>
</template>

<script>
import myToolbar from "./components/Toolbar.vue"
import NavDrawer from "./components/NavigationDrawer.vue"
export default {
  name: 'App',
  components:{
    myToolbar,
    NavDrawer,
  },
  data: () => ({
  }),
  
};
</script>

<style scoped>

</style>