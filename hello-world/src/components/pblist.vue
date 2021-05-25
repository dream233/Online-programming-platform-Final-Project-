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
	export default {
	    data() {
	      return {
	        tableData: [{
	          id: '00000001'
	        },
			{
				id: '00000002'
			},
			{
				id: '00000003'
			},
			{
				id: '00000004'
			}],
			
	      }
	    },
		methods: {
			moveto(path){
				var information = this.$route.query.information;
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
			open1(id){
				 this.$prompt('请输入密码', '提示', {
				           confirmButtonText: '确定',
				           cancelButtonText: '取消',
				           // inputPattern: /[\w!#$%&'*+/=?^_`{|}~-]+(?:\.[\w!#$%&'*+/=?^_`{|}~-]+)*@(?:[\w](?:[\w-]*[\w])?\.)+[\w](?:[\w-]*[\w])?/,
						   inputValidator(value){
							   //题目id直接用参数id表示，密码用value表示
							   //判断是否符合，如果符合返回true进入判断条件
							   if(value=="1") return true;
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
					 //这里判断该题目是不是这个面试官创建的
					 //用information.name表示用户邮箱
					 //id表示题目id，判断是否符合
					 //如果不符合，返回true
					 if(1!=1){
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
						 							   if(value=="1") return true;
						 							   else return false;
						 						   },
						           inputErrorMessage: '密码错误'
						         }).then(({ value }) => {
						           this.$message({
						             type: 'success',
						             message: '题目id为' + id
						           });
						 						   //这里加上判断是否为创建人
						 						   //if(......)
						 						   this.moveto('/loginSuccess/problemEditor');
						         }).catch(() => {
						           this.$message({
						             type: 'info',
						             message: '取消输入'
						           });       
						         });
					 }
				 }
			}
		}
	  }
</script>

<style>
</style>
