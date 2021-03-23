import Vue from "vue";
import App from "./App.vue";
import router from "./router";
import VueParticlesBg from "particles-bg-vue";
import BootstrapVue from 'bootstrap-vue/dist/bootstrap-vue.esm';
import { store } from './store/store'

import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'


Vue.use(BootstrapVue);
Vue.use(VueParticlesBg);

Vue.config.productionTip = false;

// new Vue({
//   el: '#app',
//   data: {
//     showNav: false
//   }
// });

new Vue({
  router,
  store,
  render: h => h(App)
}).$mount("#app");

// new Vue({
//   el: '#app',
//   store,
//   components: { App },
//   template: '<App/>'
// })