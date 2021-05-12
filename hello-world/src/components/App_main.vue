<template>
	<div id="app">
		
	<!-- 标题 -->
    <el-row  class="row-header" type="flex" justify="center" >
		<el-col :span="15" >
			<h2 class='header-h2'>{{ pj_name }}</h2>
		</el-col>
    </el-row>
	
	<!-- 顶部导航栏 -->
	<el-row  class="row-header" type="flex" justify="center" >
		<el-col :span="15" >
			<h2 class='header-h2'>预留为顶部导航栏</h2>
		</el-col>
	</el-row>

	
	<el-row style="background:#eeeeee" type="flex" >
		
		<!-- 这些card目前是占位用的，无实际意义 -->
		<!-- 面试题显示区域 -->
		<el-col :span="5">
			<el-card  v-for="heading in headings" :key=heading>
			  <h2>{{heading}}</h2>
			  <p>面试题显示区域</p>
			  <el-button size="small">View details >></el-button>
			</el-card>
		</el-col>
		
		<!-- 候选人写代码的区域 -->
		<el-col :span="15" style="background:grey">
			<el-card  v-for="heading in headings" :key=heading>
			  <h2>{{heading}}</h2>
			  <p>候选人写代码的区域</p>
			  <el-button size="small">View details >></el-button>
			</el-card>
		</el-col>
		
		<!-- 视频区域（要是有的话） -->
		<el-col :span="4">
			<el-card  v-for="heading in headings" :key=heading>
			  <h2>{{heading}}</h2>
			  <p>视频区域（要是有的话）</p>
			  <el-button size="small">View details >></el-button>
			</el-card>
		</el-col>
	</el-row>
	
	
	<!-- 页尾  -->
	<el-row style="background:#eeeeee" type="flex" justify="center" >
		<el-col :span="15" >
			<el-divider></el-divider>
			<p>© 2020 Company, Inc.</p>
		</el-col>
	</el-row>
	
	
	</div>
</template>

<script>
import Vue from 'vue';
    export default {
        data() 
        {
            return {
                headings:['1Heading','2Heading'],
                welcome: '欢迎来到我们的(伪)牛客面试项目',
                pj_name: '(伪)牛客面试'
            };
        },
        methods: {
			
        }
    }
</script>

<style>
	html, body,#app,el-container {
	    width: 100%;
	    height: 100%;
	    padding: 0;
	    margin: 0;
	}
	.el-card{
		background:#fbfbfb;
		width: 300px;
		display: inline-block;
		margin: 0.3em;
		border-radius:20px;
	}
	.grid-content {
		border-radius: 4px;
		min-height: 80px;
	}
	.text {
		font-size: 14px;
	}
	.item {
		padding: 18px 0;
	}
	.header-h2{
		color:#d1d1d1 ;
	}
	.header-h2:hover{
		color:#fff ;
	}
	.row-header{
		background:#409eff;
	}
	
</style>
  