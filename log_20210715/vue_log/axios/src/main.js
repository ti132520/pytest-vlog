
import App from './App.vue'
import router from './router'
import vuetify from "vue-cli-plugin-vuetify/generator/templates/default/src/plugins/vuetify";

Vue

new Vue({
    vuetify,
    router,
    render: h => h(App)
}).$mount('#app')
