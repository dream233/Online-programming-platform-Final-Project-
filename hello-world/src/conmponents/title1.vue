<template>
	<div>
		<el-menu
		  :default-active="activeIndex2"
		  class="el-menu-demo"
		  mode="horizontal"
		  @select="handleSelect"
		  background-color="#545c64"
		  text-color="#fff"
		  active-text-color="#ffd04b">
		  <el-menu-item index="1" @click="moveto('/login');notshow()">登录</el-menu-item>
		  <el-menu-item index="2" disabled>查看联系人</el-menu-item>
		  <el-menu-item index="3" disabled>参与笔试</el-menu-item>
		  <el-menu-item index="4" @click="moveto('/aboutus');notshow()">关于我们</el-menu-item>
		</el-menu>
		<div v-show="containerShow">
			<el-container>
			  <el-aside width="200px">这里是线上笔试平台</el-aside>
			  <el-container>
			    <el-header>上线时间：xxxxxx</el-header>
			    <el-main>这里写一些介绍</el-main>
			    <el-footer>联系方式：13535549796</el-footer>
			  </el-container>
			</el-container>
		</div>
	</div>
</template>

<script>
	export default {
	    data() {
	      return {
	        activeIndex: '1',
	        activeIndex2: '1',
			containerShow: '1'
	      };
	    },
	    methods: {
	      handleSelect(key, keyPath) {
	        console.log(key, keyPath);
	      },
		  moveto(path){
			  this.$router.push(path);
		  },
		  notshow(){
			  this.containerShow=0;
		  }
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
	    line-height: 200px;
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
	  
	  .el-container:nth-child(5) .el-aside,
	  .el-container:nth-child(6) .el-aside {
	    line-height: 260px;
	  }
	  
	  .el-container:nth-child(7) .el-aside {
	    line-height: 320px;
	  }
</style>
