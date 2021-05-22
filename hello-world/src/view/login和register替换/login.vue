<template>
  <div >
	  <el-row class="box"></el-row>
	  
    <el-row type="flex" justify="center" align="middle">
    <!-- justify 对齐方式 -->
		<el-card shadow="always" >
			<h1 style="text-align: center;">登录/注册</h1>
			<el-divider></el-divider>
			<!-- form表单 -->
			<el-form  :model="information" ref="information" label-width="100px" class="demo-ruleForm">
			  <!-- 用户名 -->
			  <el-form-item
				  label="用户名"
				  prop="name"
				  :rules="[
				  { required: true, message: '用户名不能为空'},
				  ]"
			  >
				  <el-input placeholder="请输入用户名" type="text" v-model="information.name" autocomplete="off"></el-input>
			  </el-form-item>

			  <!-- 密码 -->
			  <el-form-item
				  label="密码"
				  prop="password"
				  :rules="[
				  { required: true, message: '密码不能为空'},
				  ]"
			  >
				  <el-input placeholder="请输入密码" v-model="information.password" show-password></el-input>
			  </el-form-item>
			  
			  <!-- 选择身份-->
			  <div align="middle">
				  <el-radio v-model="information.id" label="candidate">候选人</el-radio>
				  <el-radio v-model="information.id" label="interviewer">面试官</el-radio>
			  </div>
			  <!-- 按钮 -->
			  <el-form-item>
				  <el-button type="primary" @click="loginning('information')">登录</el-button>
				  <el-button @click="moveto('/register')">注册</el-button>
			  </el-form-item>
			</el-form>

		</el-card>
    </el-row>


  </div>
  

</template>

<script>
import title1 from '../components/title1.vue';
import axios from 'axios';
import Vue from 'vue';
    export default {
        data() 
        {
            return {
                information: 
                {
                name: '',
                password: '',
				id: ''
                }
            };
        },
        methods: {
			moveto(path){
						  this.$router.push(path);
			},
            loginning(formName) 
            {
				this.$refs[formName].validate((valid) =>
				{
					if (valid) {
					const path = 'http://192.168.1.200:5000/login';
					axios.post(path,this.information)
						.then((res)=>{
							console.log(res.data.message);
							if(res.data.message=='Y'){
								this.moveto('/loginSuccess');
							}
							else{
								alert('请检查用户名、密码和身份后再试！');
							}
						})
						.catch((error)=>{
							console.log(error);
					})
					
					}
				});
      //           this.$refs[formName].validate((valid) => 
      //               {
      //                   if (valid) 
      //                   {
						// 	if(this.information.name=="1"&&this.information.password=="1"&&this.information.id=="candidate"){
						// 		alert('Name:'+this.information.name+';Password:'+this.information.password);
						// 		alert(this.information.name+'登录成功！');
						// 		this.moveto('/loginSuccess');
						// 	}
						// 	else if(this.information.name=="2"&&this.information.password=="2"&&this.information.id=="interviewer"){
						// 		alert('Name:'+this.information.name+';Password:'+this.information.password);
						// 		alert(this.information.name+'登录成功！');
						// 		this.moveto('/loginSuccess');
						// 	}
						// 	else{
						// 		alert('信息有误！！！！');
						// 	}
      //                   } 
						// else{
      //                       console.log('error submit!!');
      //                       return false;
      //                   }
      //               }
      //           );
            }
		},
		created(){
			window.that=this
		},
		components:{
			//title1
		}
    }
</script>

<style>
	html,body{
		height:100%;
	}
	.box{ 
		height: 100px;
	}
	.el-radio-group{
		display: flex;
		margin: 20px;
		/* 边缘 */
		justify-content: center;
	}
	.el-card{
		border-radius:30px;
		width: 450px;
	}

</style>