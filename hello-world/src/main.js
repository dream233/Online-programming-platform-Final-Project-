import Vue from 'vue';
import ElementUI from 'element-ui';
import 'element-ui/lib/theme-chalk/index.css';
import App from './App.vue';
import router from './router.js'

import VueCodemirror from 'vue-codemirror'
// import base style
import 'codemirror/lib/codemirror.css'

Vue.config.productionTip = false

Vue.use(ElementUI);
Vue.use(VueCodemirror);

new Vue({
  router:router,
  render: h => h(App),
}).$mount('#app')
