import Vue from 'vue';
import App from './App.vue';
import router from './router.js'
import globalVariable from '@/api/globalVariable.js'

import ElementUI from 'element-ui';
import 'element-ui/lib/theme-chalk/index.css';

import VueCodemirror from 'vue-codemirror'
import 'codemirror/lib/codemirror.css'

import VueQuillEditor from 'vue-quill-editor'
import 'quill/dist/quill.core.css'
import 'quill/dist/quill.snow.css'
import 'quill/dist/quill.bubble.css'

Vue.config.productionTip = false
Vue.prototype.global = globalVariable

Vue.use(ElementUI);
Vue.use(VueCodemirror);

Vue.use(VueQuillEditor, );

new Vue({
  router:router,
  render: h => h(App),
}).$mount('#app')
