import Vue from 'vue'
import Vuex from 'vuex'
import App from './App.vue'
import router from './router'
import axios from 'axios'
import VueAxios from 'vue-axios'
import vuetify from './plugins/vuetify'
import VueApexCharts from 'vue-apexcharts'

Vue.config.productionTip = false;

Vue.use(VueAxios, axios)
Vue.use(VueApexCharts)
Vue.component('apexchart', VueApexCharts)

Vue.use(Vuex);
const store = new Vuex.Store({
  state: {
    theme: false,
  }
});

new Vue({
  router,
  vuetify,
  store,
  render: h => h(App)
}).$mount('#app')
