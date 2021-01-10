import Vue from "vue";
import vuetify from "./plugins/vuetify";
import vgl from "vue-golden-layout";
import "golden-layout/src/css/goldenlayout-light-theme.css";

import App from "./App.vue";
import router from "./router";
import store from "./store";

Vue.config.productionTip = false;
Vue.use(vgl);

new Vue({
  router,
  store,
  vuetify,
  render: h => h(App)
}).$mount("#app");
