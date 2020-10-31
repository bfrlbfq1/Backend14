import Vue from 'vue'
import App from './App.vue'
import router from './router'
import vuetify from './plugins/vuetify';
import Vuelidate from 'vuelidate'
import axios from 'axios'

Vue.use(Vuelidate)
Vue.prototype.axios = axios

Vue.config.productionTip = false

new Vue({
  vuetify,
  router,
  render: h => h(App),
  http: {
    root: '/testcase',
    headers: {
      token: localStorage.getItem("token")
    }
  }
}).$mount('#app')
