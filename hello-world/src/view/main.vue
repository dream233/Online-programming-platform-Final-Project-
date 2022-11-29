<template>
	<div >
		<div>
			<!-- 面试官入口 -->
			
			<div  v-show="show_interviewer">
				<el-row type="flex" justify="center" align="middle">
					<!-- justify 对齐方式 -->
					<el-card>
						<h3 style="text-align: center;">请创建或加入面试房间</h3>
						<el-divider></el-divider>
						<!-- form表单 -->
						<el-form :model="roomForm_I" ref="roomForm_I" label-width="100px">
						<!-- 房间号 -->
						<el-form-item
							label="房间号"
							prop="roomID"
							:rules="[
							{ required: true, message: '请输入8位房间号', trigger: 'blur'},
							{ min: 8, max: 8, message: '长度 8 个字符', trigger: 'blur' }
							]"
						>
							<el-input placeholder="请输入8位房间号" type="text" v-model="roomForm_I.roomID" autocomplete="off"></el-input>
						</el-form-item>

						
						<!-- 按钮 -->
						<el-form-item class="btns">
							<el-button type="primary" @click="createRoom('roomForm_I')">创建</el-button>
							<el-button @click="joinRoom('roomForm_I')">加入</el-button>
						</el-form-item>
						</el-form>

					</el-card>
				</el-row>
			</div>
			
			<!-- 候选人入口 class="box"--> 
			<div  v-show="show_candidate">
			<el-row type="flex" justify="center" align="middle">
					<!-- justify 对齐方式 -->
					<el-card>
						<h3 style="text-align: center;">请加入面试房间</h3>
						<el-divider></el-divider>
						<!-- form表单 -->
						<el-form :model="roomForm_C" ref="roomForm_C" label-width="100px">
						<!-- 房间号 -->
						<el-form-item
							label="房间号"
							prop="roomID"
							:rules="[
							{ required: true, message: '请输入8位房间号', trigger: 'blur'},
							{ min: 8, max: 8, message: '长度 8 个字符', trigger: 'blur' }
							]"
						>
							<el-input placeholder="请输入8位房间号" type="text" v-model="roomForm_C.roomID" autocomplete="off"></el-input>
						</el-form-item>

						
						<!-- 按钮 -->
						<el-form-item class="btns">
							<el-button @click="joinRoom('roomForm_C')">加入</el-button>
						</el-form-item>
						</el-form>

					</el-card>
				</el-row>
			</div>		
			<!-- 主页面模块 -->
			<div v-show="show_home" >

				<el-container >
					<!--  -->
					<el-aside width="200px">
						<seeProblem2></seeProblem2>
					</el-aside>
					
						<el-container>
						<el-header>在线编程面试平台</el-header>
						
						<!-- 代码框的位置 -->
						<code-bar height='900px'></code-bar>
						
						<el-footer>gitee仓库：https://gitee.com/lllqaq/Online-programming-platform</el-footer>
						
						</el-container>

					<el-aside width="28%">
						<chat-room></chat-room>
					</el-aside>
				</el-container>
			</div>
			
			</div>
			
		
		
		<router-view></router-view>
	</div>
</template>

<script>
	import seeProblem2 from '../components/seeProblem2.vue'
	import seeProblem from '../components/seeProblem.vue'
	import title1 from '../components/title1.vue'
	import codeBar from '../components/codeBar.vue'
	import chatRoom from '../components/chatRoom.vue'
	import axios from 'axios';

	export default{
		data(){
			return{
				name:String,
				show_interviewer: true,   //显示面试官加入/创建room模块
				show_candidate: false,    //显示候选人加入     room模块
				show_home: false,  		  //显示主页面模块
				// 这是数据绑定对象
				roomForm_I: {
					roomID: ''
				},
				roomForm_C: {
					roomID: ''
				},
				history: null
			}
		},
		created() {
			// console.log('main create')
			var information = JSON.parse(this.$route.query.information);
			// console.log(information.roomID);
			// console.log(information.history)

			//已经输入过房间号
			if(information.roomID!=='0'){
				this.show_candidate=0;
				this.show_interviewer=0;
				this.show_home=1;
				var x;
				if(this.roomForm_C.roomID===''){
					x = {roomID:this.roomForm_I.roomID};
				}
				else if(this.roomForm_I.roomID===''){
					x = {roomID:this.roomForm_C.roomID};
				}
				x = {
					roomID:information.roomID,
				}
			}
			else {//之前没输入过房间号
				this.show_candidate= information.id==='candidate'?1:0;
				this.show_interviewer=information.id==='interviewer'?1:0;
			}
		},
		methods:{
			moveto(path){
				var information = JSON.parse(this.$route.query.information);
				
				information = {
					name: information.name,
					username:information.username,
					id: information.id,
					roomID: '',
					problemid: information.problemid
				}
				
				if(information.id === 'candidate'){
					information.roomID = this.roomForm_C.roomID
				}else{
					information.roomID = this.roomForm_I.roomID
				}
				
				information = JSON.stringify(information);
				
				//路由向下一级传递信息
				this.$router.push({
					path: path,
					query: {
						information
					}
				});
			},
			createRoom(roomForm){
				this.$refs[roomForm].validate((valid) => 
                    {	
                        if (valid) 
                        {
							//点“创建”按钮，判断是否已存在
							var x = {roomID:this.roomForm_I.roomID};
							const path = this.global.baseURL + ':5000/createroom';
							axios.post(path,x)
								.then((res)=>{
									//若无，创建成功，将{ “roomID”:”111” }发送给后端，后端返回历史记录
									if(res.data.message=='N'){
										
										//创建成功
										this.$message.success('创建房间成功')
										
										//发送roomID给后端，获取聊天记录
										this.show_interviewer=false
										this.show_home=true
										this.moveto('/loginSuccess/main');
										location.reload();
										
									}
									//若已存在，弹框提醒面试官房间已存在
									else{
										this.$message.error('roomID已存在');
									}
								})
								.catch((error)=>{
									console.log(error);
							})
                        } 
						else{
                            this.$message.error('请输入8位房间号')
                            return false;
                        }
                    }
                );
			},
			joinRoom(roomForm){
				this.$refs[roomForm].validate((valid) => 
                    {
                        if (valid) 
                        {	
							var x;
							if(this.roomForm_C.roomID===''){
								x = {roomID:this.roomForm_I.roomID};
							}
							else if(this.roomForm_I.roomID===''){
								x = {roomID:this.roomForm_C.roomID};
								
							}
							
							//往后端发送roomID 的代码
							const path = this.global.baseURL + ':5000/joinroom';
							axios.post(path,x)
								.then((res)=>{
									//房间号已存在
									if(res.data.message=='Y'){
										//加入成功
										this.$message.success('成功进入房间')
										
										//发送roomID给后端，获取聊天记录
										this.history=res.data.chathistory
										console.log(res.data.chathistory)
										this.show_interviewer=false
										this.show_candidate=false
										this.show_home=true
										this.moveto('/loginSuccess/main');
										
										
										// location.reload();
										console.log("history is "+this.history)
									}
									else{
										this.$message.error('roomID不存在');
									}
								})
								.catch((error)=>{
									console.log(error);
							})
                        } 
						else{
                            this.$message.error('请输入8位房间号')
                            return false;
                        }
                    }
                );
			}
		},
		components:{
			title1,
			codeBar,
			chatRoom,
			seeProblem2
		}
	}
</script>

<style>
.box {
	width: 480px;
	height: 100px;

	border-radius: 20px;
	position: absolute;
	left: 50%;
	top: 50%;
	transform: translate(-50%, -50%);
}
.btns {
	display: flex;
	justify-content: flex-end;
}
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

	height: calc(100vh-160px); /* 这是侧框的滚动条*/
}

.el-main {
	background-color: #E9EEF3;
	color: #333;
	text-align: center;
	line-height: 160px;
}

body > .el-container {
	margin-bottom: 40px;
	height: auto;
}

	  
</style>