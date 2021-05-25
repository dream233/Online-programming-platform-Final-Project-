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
                <h1 style="text-align: center;">注册界面</h1>
                <el-divider></el-divider>
                <!-- form表单 -->
                <el-form  :model="information" status-icon :rules="rules" ref="information" label-width="100px" class="demo-information">
                  <!-- 用户名 -->
                  <el-form-item
                      label="邮箱"
                      prop="name"
                  >
                      <el-input placeholder="请输入邮箱" type="name" v-model="information.name" autocomplete="off"></el-input>
                  </el-form-item>
				  
				  <!-- 昵称-->
				  <el-form-item
				      label="昵称"
				      prop="username"
				  >
				      <el-input placeholder="请输入昵称" type="username" v-model="information.username" autocomplete="off"></el-input>
				  </el-form-item>

                  <!-- 密码 -->
                  <el-form-item
                      label="密码"
                      prop="password"
                  >
                      <el-input placeholder="请输入密码" type="password" v-model="information.password" show-password></el-input>
                  </el-form-item>
				  
				  <!-- 确认密码 -->
				  <el-form-item
				      label="确认密码"
				      prop="repassword"
				  >
				      <el-input placeholder="请确认密码" type="repassword" v-model="information.repassword" show-password></el-input>
				  </el-form-item>
				  
				  <!-- 身份 -->
				  <el-form-item
				      label="身份"
				      prop="id"
				  >
				      <el-input placeholder="请输入您的身份(candidate或interviewer)" type="id" v-model="information.id" autocomplete="off"></el-input>
				  </el-form-item>

                  <!-- 按钮 -->
                  <el-form-item>
                      <el-button type="primary" @click="submitForm('information')">提交</el-button>
                      <el-button @click="resetForm('information')">重置</el-button>
                  </el-form-item>
                </el-form>

              </el-card>
          </el-col>
    </el-row>


  </div>
  

</template>

<script>
	import Vue from 'vue';
	    export default {
	        data()
	        {
	            var checkName = (rule, value, callback) => {
					const nameRule = /[\w!#$%&'*+/=?^_`{|}~-]+(?:\.[\w!#$%&'*+/=?^_`{|}~-]+)*@(?:[\w](?:[\w-]*[\w])?\.)+[\w](?:[\w-]*[\w])?/;
	            	if(value==='') {
	            		return callback(new Error('邮箱不能为空'));
	            	}
					else if(!nameRule.test(value)){
						return callback(new Error('格式错误'));
					}
	            	else {
	            		callback();
	            	}
	            };
				var checkUsername = (rule, value, callback) => {
					if(value==='') {
						return callback(new Error('昵称不能为空'));
					}
					else {
						callback();
					}
				};
	            var checkId = (rule, value, callback) => {
	                    if (value === '') {
	                      return callback(new Error('身份不能为空'));
	                    }
						else if(!(value=='candidate'||value=='interviewer')){
							callback(new Error('请输入正确的身份信息'));
						}else {
							callback();
						}
	                  };
	                  var validatePass = (rule, value, callback) => {
	                    if (value === '') {
	                      callback(new Error('请输入密码'));
	                    } else {
	                      if (this.information.repassword !== '') {
	                        this.$refs.information.validateField('repassword');
	                      }
	                      callback();
	                    }
	                  };
	                  var validatePass2 = (rule, value, callback) => {
	                    if (value === '') {
	                      callback(new Error('请再次输入密码'));
	                    } else if (value !== this.information.password) {
	                      callback(new Error('两次输入密码不一致!'));
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
						if(valid){
							//这里传入name username id password即可
							//通过name判断用户是否注册过，如果是新用户则返回true，进入if判断条件
							if(!(this.information.name=="1@qq.com")){
								alert('注册成功！！！！');
								this.moveto('/');
							}
							else{
								this.resetForm('information');
								alert('用户名重复，请重新注册！');
							}
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