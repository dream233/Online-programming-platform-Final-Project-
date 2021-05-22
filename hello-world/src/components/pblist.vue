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
			  <templete slot-scope="scope">
				  <el-button type="primary" icon="el-icon-search"  @click="open(scope.row.id)"></el-button>
			  </templete>
			</el-table-column>
			<el-table-column
			  label="编辑"
			  width="120">
			  <el-button type="primary" icon="el-icon-edit"></el-button>
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
				this.$router.push(path);
			},
			pass(){
				return true
			},
			open(id){
				 this.$prompt('请输入密码', '提示', {
				           confirmButtonText: '确定',
				           cancelButtonText: '取消',
				           // inputPattern: /[\w!#$%&'*+/=?^_`{|}~-]+(?:\.[\w!#$%&'*+/=?^_`{|}~-]+)*@(?:[\w](?:[\w-]*[\w])?\.)+[\w](?:[\w-]*[\w])?/,
						   inputValidator(value){
							   if(value=="1") return true;
							   else return false;
						   },
				           inputErrorMessage: '密码错误'
				         }).then(({ value }) => {
				           this.$message({
				             type: 'success',
				             message: '题目id为' + id
				           });
						   this.moveto('/loginSuccess/aboutus');
				         }).catch(() => {
				           this.$message({
				             type: 'info',
				             message: '取消输入'
				           });       
				         });
			}
		}
	  }
</script>

<style>
</style>
