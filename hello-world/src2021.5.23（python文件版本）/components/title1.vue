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
		  <el-menu-item index="1" @click="moveto('/loginSuccess')">首页</el-menu-item>
		  <el-menu-item index="2" @click="moveto('/loginSuccess/main')">联系人</el-menu-item>
		  <el-menu-item index="3" @click="moveto('/loginSuccess/pblist')">面试题汇总</el-menu-item>
		  <el-menu-item index="4" @click="moveto('/loginSuccess/aboutus')">关于我们</el-menu-item>
		</el-menu>
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
		  }
	    }
	  }
</script>

<style>
	
</style>
