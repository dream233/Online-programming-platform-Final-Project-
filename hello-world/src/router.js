import Vue from 'vue'
import VueRouter from 'vue-router'
import login from './view/login.vue'
import register from './view/register.vue'
import main from './view/main.vue'
import problemEditor from './components/problemEditor.vue'
import loginSuccess from './view/loginSuccess.vue'
import hellovisit from './components/hellovisit.vue'
import pblist from './components/pblist.vue'
import seeProblem from './components/seeProblem.vue'
import problemCreate from './components/problemCreate.vue'
import forgetpwd from './view/forgetpwd.vue'

Vue.use(VueRouter)

const originalPush = VueRouter.prototype.push
VueRouter.prototype.push = function push (location) {
  return originalPush.call(this, location).catch(err => err)
}

const router = new VueRouter({
	routes:[
		{
			path:'/',
			name:'login',
			component:login			
		},
		{
			path:'/forgetpwd',
			name:'forgetpwd',
			component:forgetpwd
		},
		{
			path:'/main',
			name:'main',
			component:main			
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
				},
				{
					path: 'problemEditor/:id/:password',
					component: problemEditor
				},
				{
					path: 'seeProblem/:id/:password',
					component: seeProblem
				},
				{
					path: 'problemCreate',
					component: problemCreate
				}
			]
		}
	]
})


export default router