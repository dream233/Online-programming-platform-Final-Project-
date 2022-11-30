<template>
  <div>
    <el-row type="flex" justify="center">
      <!-- justify 对齐方式 -->
      <el-col :span="6">
        <div class="grid-content"></div>
      </el-col>
    </el-row>

    <el-row type="flex" justify="center">
    <!-- justify 对齐方式 -->
          <el-col :span="9">
              <el-card shadow="always" >
                <h1 style="text-align: center;">register</h1>
                <el-divider></el-divider>
                <!-- form表单 -->
                <el-form  :model="information" status-icon :rules="rules" ref="information" label-width="100px" class="demo-information">
                  <!-- 用户名 -->
                  <el-form-item
                      label="email"
                      prop="name"
                  >
                      <el-input placeholder="please input email" type="name" v-model="information.name" autocomplete="off"></el-input>
                  </el-form-item>
				  
				  <!-- 昵称-->
				  <el-form-item
				      label="username"
				      prop="username"
				  >
				      <el-input placeholder="please input username" type="username" v-model="information.username" autocomplete="off"></el-input>
				  </el-form-item>

                  <!-- 密码 -->
                  <el-form-item
                      label="password"
                      prop="password"
                  >
                      <el-input placeholder="please input password" type="password" v-model="information.password" show-password></el-input>
                  </el-form-item>
				  
				  <!-- 确认密码 -->
				  <el-form-item
				      label="confirm password"
				      prop="repassword"
				  >
				      <el-input placeholder="please confirm password" type="repassword" v-model="information.repassword" show-password></el-input>
				  </el-form-item>
				  
				  <!-- 身份 -->
				  <div align="middle">
				  				  <el-radio v-model="information.id" label="candidate">candidate</el-radio>
				  				  <el-radio v-model="information.id" label="interviewer">interviewer</el-radio>
				  </div>

                  <!-- 按钮 -->
                  <el-form-item>
                      <el-button type="primary" @click="submitForm('information')">submit</el-button>
                      <el-button @click="resetForm('information')">reset</el-button>
                  </el-form-item>
                </el-form>

              </el-card>
          </el-col>
    </el-row>


  </div>
  

</template>

<script>
	import Vue from 'vue';
	import axios from 'axios';
	    export default {
	        data()
	        {
	            var checkName = (rule, value, callback) => {
					const nameRule = /[\w!#$%&'*+/=?^_`{|}~-]+(?:\.[\w!#$%&'*+/=?^_`{|}~-]+)*@(?:[\w](?:[\w-]*[\w])?\.)+[\w](?:[\w-]*[\w])?/;
	            	if(value==='') {
	            		return callback(new Error('E-mail can not be empty'));
	            	}
					else if(!nameRule.test(value)){
						return callback(new Error('wrong format'));
					}
	            	else {
	            		callback();
	            	}
	            };
				var checkUsername = (rule, value, callback) => {
					if(value==='') {
						return callback(new Error('username can not be blank'));
					}
					else {
						callback();
					}
				};
	            var checkId = (rule, value, callback) => {
	                    if (value === '') {
	                      return callback(new Error('Identity cannot be empty'));
	                    }
						else if(!(value=='candidate'||value=='interviewer'||value=='1'||value=='2')){
							callback(new Error('Please enter correct identity information'));
						}else {
							callback();
						}
	                  };
	                  var validatePass = (rule, value, callback) => {
	                    if (value === '') {
	                      callback(new Error('please enter password'));
	                    } else {
	                      if (this.information.repassword !== '') {
	                        this.$refs.information.validateField('repassword');
	                      }
	                      callback();
	                    }
	                  };
	                  var validatePass2 = (rule, value, callback) => {
	                    if (value === '') {
	                      callback(new Error('please enter password again'));
	                    } else if (value !== this.information.password) {
	                      callback(new Error('The passwords entered twice are inconsistent!'));
	                    } else {
	                      callback();
	                    }
	                  };
				return {
	                information: 
	                {
	                name: '',
					username: '',
	                password: '',
					id: '',
					repassword: ''
	                },
					rules:{
						name:[
							{
								validator: checkName, trigger:'blur'
							}
						],
						password: [{
							validator: validatePass, trigger:'blur'
						}],
						repassword: [{
							validator: validatePass2, trigger:'blur'
						}],
						id: [{
							validator: checkId, trigger:'blur'
						}],
						username: [{
							validator: checkUsername, trigger:'blur'
						}],
					}
					
					
	            };
	        },
	        methods: {
				moveto(path){
							  this.$router.push(path);
				},
	        	resetForm(formName) {
	        	    this.$refs[formName].resetFields();
	        	},
				submitForm(formName) {
				    this.$refs[formName].validate((valid) => {
						if(this.information.id==''){
							this.$message({
							          message: 'No identity selected!',
							          type: 'warning'
							        });
							valid=!valid;
						}
						if(valid){
							console.log('y')
							const path = this.global.baseURL +':5000/register';
							axios.post(path,this.information)
								.then((res)=>{
									if(res.data.message=='Y'){
										this.$message({
										          message: 'registration success! Please go to the mailbox to activate!',
										          type: 'success'
										        });
										this.moveto('/');
									}
									else if(res.data.message=='N'){
										this.resetForm('information');
										this.$message({
										          message: 'The email address is duplicated, please register again!',
										          type: 'warning'
										        });
									}
								})
								.catch((error)=>{
									console.log(error);
							})
							//这里传入name username id password即可
							//通过name判断用户是否注册过，如果是新用户则返回true，进入if判断条件
						}
						else{
							console.log('error submit!!');
							return false;
						}
				    });
				}
	        }
	    }
</script>

<style>
  .el-radio-group{
    display: flex;
    margin: 20px;
    /* 边缘 */
    justify-content: center;
    
  }
  .el-card{
    border-radius:30px;
    width: 450px;
    /* box-shadow: 0 2px 12px 0 rgb(243, 102, 102); */
    /* box-shadow: 0 2px 4px rgba(0, 0, 0, .12), 0 0 6px rgba(0, 0, 0, .04); */
  }
  .grid-content {
    /* background: rgb(14, 214, 131); */
    border-radius: 4px;
    min-height: 10px;
  }
  .el-row {
    margin-bottom: 20px;
  }
  
</style>