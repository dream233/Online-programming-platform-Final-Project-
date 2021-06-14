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
		  <el-submenu index="3">
			  <template slot="title">
				  面试题
			  </template>
			  <el-menu-item index="3-1" @click="moveto('/loginSuccess/pblist')">面试题汇总</el-menu-item>
			  <el-menu-item index="3-2" @click="newProblem()">新建面试题</el-menu-item>
		  </el-submenu>
		  <el-menu-item index="4" @click="moveto('/loginSuccess/aboutus')">关于我们</el-menu-item>
		  
		  <el-menu-item index="5" @click="test()">个人信息</el-menu-item>
		</el-menu>
	</div>
</template>

<script>
	export default {
	    data() {
	      return {
	        activeIndex: '1',
	        activeIndex2: '1',
			containerShow: '1',
			information:{},
	      };
	    },
	    methods: {
	      handleSelect(key, keyPath) {
	        // console.log(key, keyPath);
	      },
		  moveto(path){
			  var information = this.$route.query.information;
			  this.$router.push({
				  path: path,
				  query: {
					  information
				  }
			  });
		  },
		  newProblem(){
			  //这里if条件判断当前用户的id
			  var information = this.$route.query.information;
			  information = JSON.parse(information);
			  if(information.id=='candidate'){
				   this.$message({
				            showClose: true,
				            message: '只有面试官有权限',
				            type: 'warning',
							// center: true
				          });
			  }else{
				  var information = this.$route.query.information;
				  this.moveto('/loginSuccess/problemCreate');
			  }
		  },
		  test(){		  
			  var information = this.information;
			  alert("当前用户邮箱："+ information.name + "用户名： " + information.username + "用户身份： " + information.id)
		  }
	    },
		created(){		
		  var information = JSON.parse(this.$route.query.information);
		  this.information =information	  
		}
		
	  }
</script>

<style>
	
</style>
