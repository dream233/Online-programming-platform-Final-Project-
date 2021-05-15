import Vue from 'vue'
import VueRouter from 'vue-router'
import goto1 from './view/goto1.vue'
import login from './view/login.vue'
import aboutus from './view/aboutus.vue'
import register from './view/register.vue'

Vue.use(VueRouter)

const router = new VueRouter({
	routes:[
		{
			path:'/login',
			name:'login',
			component:login			
		},
		{
			path:'/goto1',
			name:'goto1',
			component:goto1
		},
		{
			path:'/aboutus',
			name:'aboutus',
			component:aboutus
		},
		{
			path:'/register',
			name:'register',
			component:register
		}
	]
})


export default router