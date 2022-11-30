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
		  <el-menu-item index="1" @click="moveto('/loginSuccess')">home</el-menu-item>
		  <el-menu-item index="2" @click="moveto('/loginSuccess/main')">join room</el-menu-item>
		  <el-submenu index="3">
			  <template slot="title">
				  problem
			  </template>
			  <el-menu-item index="3-1" @click="moveto('/loginSuccess/pblist')">Summary of interview questions</el-menu-item>
			  <el-menu-item index="3-2" @click="newProblem()">Create a new interview question</el-menu-item>
		  </el-submenu>
		  <el-menu-item index="4" @click="moveto2('/')">exit</el-menu-item>
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
		  moveto2(path){
		  	this.$router.push(path);
		  },
		  newProblem(){
			  //这里if条件判断当前用户的id
			  var information = this.$route.query.information;
			  information = JSON.parse(information);
			  if(information.id=='candidate'){
				   this.$message({
				            showClose: true,
				            message: 'Only the interviewer has permission',
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
			  alert("Current user mailbox:"+ information.name + "username: " + information.username + "user ID: " + information.id)
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
