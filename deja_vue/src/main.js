import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import axios from 'axios'

// axios.defaults.baseURL = 'https://apidejavue.com/'
axios.defaults.baseURL =  'http://'+location.hostname+':8000'

createApp(App).use(store).use(router, axios).mount('#app')
