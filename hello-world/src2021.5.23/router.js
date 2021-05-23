import Vue from 'vue'
import VueRouter from 'vue-router'
import goto1 from './view/goto1.vue'
import login from './view/login.vue'
import aboutus from './view/aboutus.vue'
import register from './view/register.vue'
import main from './view/main.vue'
import problemEditor from './components/problemEditor.vue'
import loginSuccess from './view/loginSuccess.vue'
import hellovisit from './components/hellovisit.vue'
import pblist from './components/pblist.vue'

Vue.use(VueRouter)

const router = new VueRouter({
	routes:[
		{
			path:'/',
			name:'login',
			component:login			
		},
		{
			path:'/main',
			name:'main',
			component:main			
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
		},
		{
			path: '/problemEditor',
			name: 'problemEditor',
			component: problemEditor
		},
		{
			path: '/loginSuccess',
			name: 'loginSuccess',
			component: loginSuccess,
			children:[
				{
					path: 'aboutus',
					component: aboutus
				},
				{
					path: 'main',
					component: main
				},
				{
					path: '',
					component: hellovisit
				},
				{
					path: 'pblist',
					component: pblist
				}
			]
		}
	]
})


export default router