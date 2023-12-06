import Vue from 'vue'
import App from './App.vue'
import router from './router'

Vue.config.productionTip = false

import axios from 'axios'
Vue.prototype.$axios = axios

import cookies from 'vue-cookies'
Vue.prototype.$cookies = cookies

import './assets/css/global.css'

import settings from './assets/js/settings'
Vue.prototype.$settings = settings

import 'bootstrap'

new Vue({
    router,
    render: h => h(App)
}).$mount('#app')