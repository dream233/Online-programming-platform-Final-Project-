<template>
	<div>
			<div class="edit_container">
			        <quill-editor 
			            v-model="content"
			            ref="myQuillEditor" 
			            :options="editorOption" 
			            @blur="onEditorBlur($event)" @focus="onEditorFocus($event)"
			            @change="onEditorChange($event)">
			        </quill-editor>
					<el-button type="primary" @click="saveHtml">保存<i class="el-icon-upload el-icon--right"></i></el-button>
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
	export default {
	  name: 'App',
	  data(){
	     return {
	                 content: `<p>题目未响应，信息有误！</p>`,
	                 editorOption: {
	                   modules:{
	                               toolbar:[
	                                 ['bold', 'italic', 'underline', 'strike'],    //加粗，斜体，下划线，删除线
	                                 ['blockquote', 'code-block'],     //引用，代码块
	                     
	                     
	                                 [{ 'header': 1 }, { 'header': 2 }],        // 标题，键值对的形式；1、2表示字体大小
	                                 [{ 'list': 'ordered'}, { 'list': 'bullet' }],     //列表
	                                 [{ 'script': 'sub'}, { 'script': 'super' }],   // 上下标
	                                 [{ 'indent': '-1'}, { 'indent': '+1' }],     // 缩进
	                                 [{ 'direction': 'rtl' }],             // 文本方向
	                     
	                     
	                                 [{ 'size': ['small', false, 'large', 'huge'] }], // 字体大小
	                                 [{ 'header': [1, 2, 3, 4, 5, 6, false] }],     //几级标题
	                     
	                     
	                                 [{ 'color': [] }, { 'background': [] }],     // 字体颜色，字体背景颜色
	                                 [{ 'font': [] }],     //字体
	                                 [{ 'align': [] }],    //对齐方式
	                     
	                     
	                                 ['clean'],    //清除字体样式
	                                 ['image']    //上传图片
	                     
	                               ],
								   imageResize: {
									   displayStyles: {
									                   backgroundColor: 'black',
									                   border: 'none',
									                   color: 'white'
									                 },
									                 modules: [ 'Resize', 'DisplaySize', 'Toolbar' ]
								   }
	                             },
	                             //theme:'snow'
	                           }
	                 }
	             },
		computed: {
	        editor() {
	            return this.$refs.myQuillEditor.quill;
	        },
	    },
		methods: {
	        onEditorReady(editor) { // 准备编辑器
	        },
	        onEditorBlur(){}, // 失去焦点事件
	        onEditorFocus(){}, // 获得焦点事件
	        onEditorChange(){}, // 内容改变事件
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
	    //     saveHtml:function(event){
	    //       alert(this.content);
			  // console.log(this.content);
	    //     },
			saveHtml(){
				var information = JSON.parse(this.$route.query.information);
				const path = this.global.baseURL + ':5000/problemEdit';
				var probleminfor = {
					ProblemID:this.$route.params.id,
					contents:this.content,
				};
				// console.log(probleminfor)
				axios.post(path,probleminfor)
					.then((res)=>{
						if(res.data.message=='Y'){
							this.$message({
							          showClose: true,
							          message: '题目修改成功',
							          type: 'success'
							        });
							this.moveto("/loginSuccess/pblist");
						}
						else{
							this.$message({
							          showClose: true,
							          message: '存在某些未知的问题，修改失败',
							          type: 'warning'
							        });
						}
					})
			}
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
			console.log('*********************');
			console.log(this.$route.params.id);
			axios.post(path,tem)
				.then((res)=>{
					console.log(res.data.password);
					console.log('*********************');
					pp=res.data.password;
					if(this.$route.params.password==pp){
						
						//如果符合，那么调用题目内容（即一大串字符串），然后this.message=内容（下面那些内容用于测试，可以删掉）
						this.content= res.data.contents;
					}
				});
		}
	}
</script>

<style>
	
</style>