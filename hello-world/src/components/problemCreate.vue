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
					<el-button type="primary" @click="dialogFormVisible = true">创建<i class="el-icon-upload el-icon--right"></i></el-button>
					
					<el-dialog title="题目信息(用于创建题目权限)" :visible.sync="dialogFormVisible">
					  <el-form :model="information">
					    <el-form-item label="题目id" :label-width="formLabelWidth">
					      <el-input type="text" placeholder="请输入8位数字id" 
						  v-model="pinformation.id" show-word-limit autocomplete="off" maxlength="8"></el-input>
					    </el-form-item>
					    <el-form-item label="题目密码" :label-width="formLabelWidth">
					      <el-input v-model="pinformation.password" autocomplete="off"></el-input>
					    </el-form-item>
					  </el-form>
					  <div slot="footer" class="dialog-footer">
					    <el-button @click="dialogFormVisible = false">取 消</el-button>
					    <el-button type="primary" @click="dialogFormVisible = false;saveHtml()">确 定</el-button>
					  </div>
					</el-dialog>
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
	                 content: ``,
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
	                           },
							   dialogFormVisible: false,
							           pinformation: {
							             id: '',
										 password: '',
							           },
							           formLabelWidth: '120px'
	                 };
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
			saveHtml(){
				var information = JSON.parse(this.$route.query.information);
				const path = this.global.baseURL + ':5000/problemEdit';
				var probleminfor = {
					ProblemID:this.$route.params.id,
					contents:this.content,
				};
				axios.post(path,probleminfor)
					.then((res)=>{
						if(res.data.message=='Y'){
							this.$message({
							          showClose: true,
							          message: '题目创建成功',
							          type: 'success'
							        });
						}
						else{
							this.$message({
							          showClose: true,
							          message: '题目id已存在',
							          type: 'warning'
							        });
						}
					})
			  //这里判断题目是否已存在
			  //this.pinformation.id表示题目id
			  //this.pinformation.password表示题目密码
			  //如果不是已存在，那么返回true，替换下面的判断条件
			  /*const path = 'http://111.229.68.117:5000/problemCreate';
			  axios.post(path,this.pinformation.id)
					.then((res)=>{
						
					})*/
			  /* if(!(this.pinformation.id=='1')){
				  this.$message({
				            showClose: true,
				            message: '题目创建成功',
				            type: 'success'
				          });
				  //这里把this.content存入对应的题目id里，this.content为内容
				  //
				  
			  }
			  else {
				  this.$message({
				            showClose: true,
				            message: '题目id已存在',
				            type: 'warning'
				          });
			  } */
			}
	    },
		created(){
			window.that=this;
			
		}
	}
</script>

<style>
	
</style>