<template>
	<div >
		<div>		
			<!-- 主页面模块 -->
			<div>
				<el-container>
					<!--  -->
					<el-aside width="200px">
						<student_problem></student_problem>
					</el-aside>
					
						<el-container>
						<el-header>虚假的牛客网站，贼牛xxxxxx</el-header>
						
						<!-- 代码框的位置 -->
						<code-bar></code-bar>
						
						<el-footer>联系方式：13535549796</el-footer>
						
						</el-container>

					<el-aside width="200px">聊天框的位置</el-aside>
				</el-container>
			</div>
			
			</div>
			
		<!-- 登录界面跳转（测试） -->
		<button @click="moveto('/login')">点击进入登录/注册界面</button>
		<!-- 测试......跳转到创建/编辑题目界面 -->
		<button @click="moveto('/problemEditor')">点击进入题目创建/编辑界面</button>
		
		<router-view></router-view>
	</div>
</template>

<script>
	import student_problem from '../components/student_problem.vue'
	import title1 from '../components/title1.vue'
	import codeBar from '../components/codeBar.vue'
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
			title1,
			codeBar,
			student_problem
		}
	}
</script>

<style>
	.el-header, .el-footer {
	    background-color: #B3C0D1;
	    color: #333;
	    text-align: center;
	    line-height: 60px;
	  }
	  
	  .el-aside {
	    background-color: #D3DCE6;
	    color: #333;
	    text-align: center;
	    /* line-height: 200px; */
		height: calc(100vh - 160px); /* 这是侧框的滚动条*/
	  }
	  
	  .el-main {
	    background-color: #E9EEF3;
	    color: #333;
	    text-align: center;
	    line-height: 160px;
	  }
	  
	  body > .el-container {
	    margin-bottom: 40px;
	  }
	  
	  
</style>