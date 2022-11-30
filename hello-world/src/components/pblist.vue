<template>
	<div>
		<el-table
		    :data="tableData"
		    stripe
		    style="width: 100%">
		    <el-table-column
		      prop="id"
		      label="problem id"
		      width="1000">
		    </el-table-column>
			<el-table-column
			  label="view problem"
			  width="120">
			  <template slot-scope="scope" >
				  <el-button type="primary" icon="el-icon-search"  @click="open1(scope.row.id)"></el-button>
			  </template>
			</el-table-column>
			<el-table-column
			  label="edit problem"
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
				var information = this.$route.query.information;
				// console.log(information);
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
					
				 this.$prompt('please input password', 'prompt', {
				           confirmButtonText: 'confirm',
				           cancelButtonText: 'cancel',
				           // inputPattern: /[\w!#$%&'*+/=?^_`{|}~-]+(?:\.[\w!#$%&'*+/=?^_`{|}~-]+)*@(?:[\w](?:[\w-]*[\w])?\.)+[\w](?:[\w-]*[\w])?/,
						   inputValidator(value){
									if(value==pp) return true;
									else return false;
						   },
				           inputErrorMessage: 'password error'
				         }).then(({ value }) => {
				           this.$message({
				             type: 'success',
				             message: 'problem id is' + id
				           });
						   this.moveto('/loginSuccess/seeProblem/'+id+'/'+value);
				         }).catch(() => {
				           this.$message({
				             type: 'info',
				             message: 'cancel input'
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
				 				            message: 'Only the interviewer has permission',
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
										  message: 'You do not have permission to edit this question',
										  type: 'warning',
										});
							}
							else{
								 this.$prompt('please enter password', 'prompt', {
									 
										   confirmButtonText: 'confirm',
										   cancelButtonText: 'cancel',
										   // inputPattern: /[\w!#$%&'*+/=?^_`{|}~-]+(?:\.[\w!#$%&'*+/=?^_`{|}~-]+)*@(?:[\w](?:[\w-]*[\w])?\.)+[\w](?:[\w-]*[\w])?/,
														   inputValidator(value){
															//这里跟上面判断题目id和密码一样
															   if(value==pp) return true;
															   else return false;
														   },
										   inputErrorMessage: 'password error'
										 }).then(({ value }) => {
										   this.$message({
											 type: 'success',
											 message: 'problem id is' + id
										   });
										   console.log(information)
											this.moveto('/loginSuccess/problemEditor/'+id+'/'+value);
										 }).catch(() => {
										   this.$message({
											 type: 'info',
											 message: 'cancel input'
										   });       
										 });
							}
					 	});
					 //Here to judge whether the topic was created by the interviewer
					 //Use information.name to represent the user mailbox
					 //id indicates the topic id, and judges whether it meets
					 //If not, return true
					
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