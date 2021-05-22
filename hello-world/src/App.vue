<template>
	<div id="app">
		<!-- 登录界面跳转（测试） -->
		<!-- <el-container>
		  <el-header>这里是一个初始界面（需要改更好看）</el-header>
		</el-container> -->
		
		<router-view></router-view>
	</div>
</template>

<script>
	import problemEditor from './components/problemEditor.vue'
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
			problemEditor
		}
	}
</script>

<style>
	.el-header {
	    background-color: #B3C0D1;
	    color: #333;
	    text-align: center;
	    line-height: 60px;
	  }
	  body > .el-container {
	      margin-bottom: 40px;
	    }
	  
</style>