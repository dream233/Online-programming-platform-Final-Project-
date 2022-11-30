<template>
</template>

<script>
</script>

<style>
</style>
<template>

	<div class="ql-container ql-snow">
	    <div class="ql-editor">
			<!-- <button @click="t">点击这里显示题目</button> -->
			<el-row>
				<el-input v-model="problemid" placeholder="please input problem id"></el-input>
				<el-button type="success" icon="el-icon-check" circle @click="seeProblem()"></el-button>
			</el-row>
			<p v-html="message"></p>
	    </div>
	</div>
</template>

<script>
	// import hljs from 'highlight.js'
	  import VueQuillEditor, { Quill } from 'vue-quill-editor'
	  // import { ImageDrop } from 'quill-image-drop-module'
	  import ImageResize from 'quill-image-resize-module'
	  import axios from 'axios';
	  // Quill.register('modules/imageDrop', ImageDrop)
	  Quill.register('modules/imageResize', ImageResize)
	export default{
		data(){
			return{
				message: '<p>The question has not been answered, the information is wrong!</p>',
				problemid: ''
			}
		},
		methods:{
			// t(){
			// 	this.message=''
			// }
			seeProblem(){
				var information = JSON.parse(this.$route.query.information);
				
				information = {
					name: information.name,
					username:information.username,
					id: information.id,
					roomID: information.roomID,
					problemid: this.problemid
				};
				information=JSON.stringify(information);
				this.$router.push({
					path: '/loginSuccess/main',
					query: {
						information
					}
				});
				location.reload();
			}
		},
		created(){
			window.that=this;
			//这里改成判断题目id密码是否符合数据库
			//this.$route.params.id表示题目id
			//this.$route.params.password表示题目密码
			//判断是否符合，符合返回true，进入判断条件
			var information = JSON.parse(this.$route.query.information);
			const path = this.global.baseURL + ':5000/problemCheck';
			var tem = {id:information.problemid};
			//console.log(this.$route.params.id);
			// console.log('seeProblem');
			axios.post(path,tem)
				.then((res)=>{
					//如果符合，那么调用题目内容（即一大串字符串），然后this.message=内容（下面那些内容用于测试，可以删掉）
					this.message= res.data.contents;
				});
			
		}
	}
</script>

<style>
</style>
