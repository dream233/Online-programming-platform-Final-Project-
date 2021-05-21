<template>
	<div id="app">	
		<!-- 登录界面跳转（测试） -->
		<button @click="ifshow=0;moveto('/main')">点击进入主界面</button>
		
		<router-view></router-view>
	</div>
</template>

<script>
	import title1 from './components/title1.vue'
	import codeBar from './components/codeBar.vue'
	import Vue from 'vue'
	export default{
		data(){
			return{
				name:String,
				ifshow: '1'
			}
		},
		methods:{
			moveto(path){
						  this.$router.push(path);
			}
		},
		components:{
		}
	}
</script>

<style>
	  
</style>