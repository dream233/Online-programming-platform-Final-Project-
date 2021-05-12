import Vue from 'vue'
import ElementUI from 'element-ui';
import 'element-ui/lib/theme-chalk/index.css';

//注意，本页面除了解除注释以外，请不要修改

//通过切换不同的import实现界面的切换（因为跳转还没有写好）
// 登陆界面，解除注释编译后就可以用
// import App from './components/App_load.vue'   

//主界面，用法同上
import App from './components/App_main.vue'


Vue.config.productionTip = false

Vue.use(ElementUI);

new Vue
(
  {
    render: h => h(App),
  }
).$mount('#app')
