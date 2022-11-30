<template>

	<div class="ql-container ql-snow">
	    <div class="ql-editor">
			<!-- <button @click="t">点击这里显示题目</button> -->
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
				message: '<p>The question has not been answered, the information is wrong!</p>'
			}
		},
		methods:{
			// t(){
			// 	this.message=''
			// }
		},
		created(){
			window.that=this;
			//这里改成判断题目id密码是否符合数据库
			//this.$route.params.id表示题目id
			//this.$route.params.password表示题目密码
			//判断是否符合，符合返回true，进入判断条件
			const path = this.global.baseURL + ':5000/problemCheck';
			var pp = '';
			var tem = {id:this.$route.params.id};
			//console.log(this.$route.params.id);
			// console.log('seeProblem');
			axios.post(path,tem)
				.then((res)=>{
					pp=res.data.password;
					if(this.$route.params.password==pp){
						
						//如果符合，那么调用题目内容（即一大串字符串），然后this.message=内容（下面那些内容用于测试，可以删掉）
						this.message= res.data.contents;
					}
				});
			
		}
	}
</script>

<style>
</style>
