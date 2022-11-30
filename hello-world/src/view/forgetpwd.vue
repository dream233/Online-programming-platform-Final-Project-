<template>
	<div >
	<el-row type="flex" justify="center" align="middle">
	<!-- justify 对齐方式 -->
		<el-card shadow="always" >
			<h1 style="text-align: center;">Forgot password</h1>
			<el-divider></el-divider>
			<!-- form表单 -->
			<el-form  :model="information" ref="information" label-width="100px" class="demo-ruleForm">
			  <!-- 用户名 -->
			  <el-form-item
				  label="email"
				  prop="email"
				  :rules="[
				  { required: true, message: 'E-mail can not be empty'},
				  ]"
			  >
				  <el-input placeholder="please input your email" type="text" v-model="information.email" autocomplete="off"></el-input>
			  </el-form-item>
			  <!-- 按钮 -->
			  <el-form-item>
				  <el-button type="primary" @click="forget('information')">confirm</el-button>
			  </el-form-item>
			</el-form>
	
		</el-card>
	</el-row>
	
	
	</div>
</template>

<script>
import Vue from 'vue';
import axios from 'axios'
export default{
	data(){
		return{
			information:
			{
			email: ''
			}
		}
	},
	methods:{
		moveto(){
			this.$router.push('/');
		},
		forget(formName){
			this.$refs[formName].validate((valid) =>
			    {
			        if (valid) 
			        {
						const path = this.global.baseURL + ':5000/forgetpassword';
						axios.post(path,{email:this.information.email})
						  .then((res) => {
							console.log(res)
						  })
						  .catch((error) => {
							console.error(error);
						});
						this.$message({
						          showClose: true,
						          message: 'Please go to your email to check the password we sent you',
						          type: 'success'
						        });
						this.moveto('/');
			        } 
					else{
			            console.log('error submit!!');
			            return false;
			        }
			    }
			);
		}
	},
	
}
</script>

<style>
</style>
