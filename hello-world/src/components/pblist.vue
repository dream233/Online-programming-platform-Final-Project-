<template>
	<div>
		<el-table
		    :data="tableData"
		    stripe
		    style="width: 100%">
		    <el-table-column
		      prop="id"
		      label="题目id"
		      width="1000">
		    </el-table-column>
			<el-table-column
			  label="查看"
			  width="120">
			  <template slot-scope="scope" >
				  <el-button type="primary" icon="el-icon-search"  @click="open1(scope.row.id)"></el-button>
			  </template>
			</el-table-column>
			<el-table-column
			  label="编辑"
			  width="120">
			  <template slot-scope="scope" >
				  <el-button type="primary" icon="el-icon-edit" @click="open2(scope.row.id)"></el-button>
			  </template>
			</el-table-column>
		  </el-table>
	</div>
</template>

<script>
	import axios from 'axios';
	export default {
	    data() {
	      return {
	        tableData: [],
			problempassword:'',
	      }
	    },
		methods: {
			moveto(path){
				var information = JSON.stringify(this.$route.query.information);
				
				this.$router.push({
					  path: path,
					  query: {
						  information
					  }
				});
				
			},
			pass(){
				return true
			},
			open1(id){/////////////////////////////////////////////////////////////////////////////////////////////
				const path = this.global.baseURL + ':5000/problemCheck';
				console.log(id);
				var pp = '';
				var tem = {id:id};
				axios.post(path,tem)
					.then((res)=>{
						//console.log(res.data.password);
						pp=res.data.password;
					});
					
				 this.$prompt('请输入密码', '提示', {
				           confirmButtonText: '确定',
				           cancelButtonText: '取消',
				           // inputPattern: /[\w!#$%&'*+/=?^_`{|}~-]+(?:\.[\w!#$%&'*+/=?^_`{|}~-]+)*@(?:[\w](?:[\w-]*[\w])?\.)+[\w](?:[\w-]*[\w])?/,
						   inputValidator(value){
									if(value==pp) return true;
									else return false;
						   },
				           inputErrorMessage: '密码错误'
				         }).then(({ value }) => {
				           this.$message({
				             type: 'success',
				             message: '题目id为' + id
				           });
						   this.moveto('/loginSuccess/seeProblem/'+id+'/'+value);
				         }).catch(() => {
				           this.$message({
				             type: 'info',
				             message: '取消输入'
				           });       
				         });
			},
			open2(id){
				 var pg = '';
				 var pp = '';
				 var information = this.$route.query.information;
				 information = JSON.parse(information);
				 if(information.id=='candidate'){
				 				   this.$message({
				 				            showClose: true,
				 				            message: '只有面试官有权限',
				 				            type: 'warning',
				 							// center: true
				 				          });
				 }
				 else{
					 const path = this.global.baseURL + ':5000/problemCheck';
					 var tem = {id:id};
					 axios.post(path,tem)
					 	.then((res)=>{
							pp=res.data.password;
					 		pg=res.data.owner;
							if(pg!=information.name){
								 this.$message({
										  showClose: true,
										  message: '您没有编辑该题的权限',
										  type: 'warning',
										});
							}
							else{
								 this.$prompt('请输入密码', '提示', {
									 
										   confirmButtonText: '确定',
										   cancelButtonText: '取消',
										   // inputPattern: /[\w!#$%&'*+/=?^_`{|}~-]+(?:\.[\w!#$%&'*+/=?^_`{|}~-]+)*@(?:[\w](?:[\w-]*[\w])?\.)+[\w](?:[\w-]*[\w])?/,
														   inputValidator(value){
															//这里跟上面判断题目id和密码一样
															   if(value==pp) return true;
															   else return false;
														   },
										   inputErrorMessage: '密码错误'
										 }).then(({ value }) => {
										   this.$message({
											 type: 'success',
											 message: '题目id为' + id
										   });
										   console.log(information)
											this.moveto('/loginSuccess/problemEditor/'+id+'/'+value);
										 }).catch(() => {
										   this.$message({
											 type: 'info',
											 message: '取消输入'
										   });       
										 });
							}
					 	});
					 //这里判断该题目是不是这个面试官创建的
					 //用information.name表示用户邮箱
					 //id表示题目id，判断是否符合
					 //如果不符合，返回true
					
				 }
			}
		},
		created(){
				const path = this.global.baseURL + ':5000/pblist';
				axios.get(path,this.information)
					.then((res)=>{
						this.tableData = res.data.pblist;
					})
		}


	  }
</script>

<style>
</style>