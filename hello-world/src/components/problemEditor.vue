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
	    //     saveHtml:function(event){
	    //       alert(this.content);
			  // console.log(this.content);
	    //     },
			saveHtml(){
			  alert(this.content);
			  console.log(this.content);
			}
	    },
		created(){
			window.that=this;
			this.content='<ul><li><strong><em><u>dkfjlskdjfkslf</u></em></strong></li><li><strong><em><u>附件是立刻搭街坊立刻是</u></em></strong></li><li><strong><em><u>是独立开发炯之女会计出纳在</u></em></strong></li><li><strong><em><u>法律搭街坊立刻就在芬兰空军的离开这世界</u></em></strong></li></ul><p><strong><em><u>dk附件是的JFK老师的</u></em></strong></p><p><br></p><p><br></p><p><br></p><p><strong><em><u>首都基辅罗斯大家来看</u></em></strong></p><p><strong><em><u>搭街坊昆仑山觉得</u></em></strong></p><p><br></p><p><br></p><p><br></p><p><br></p><p><br></p><p><br></p><p><br></p><p><br></p><p><strong><em><u>打卡时间分厘卡圣诞节饭卡里说的你看     方式决定离开房间昆仑山大家</u></em></strong></p><p><strong><em>但是看了方式</em></strong></p><p><br></p><p><br></p><p><br></p><p><strong><em>出行距离空间kl</em></strong></p><p><br></p><p><strong><em>发就可怜见立刻就 JFK四点零分记录卡撒旦解放开始JFK老师讲课靠靠靠靠靠靠靠靠靠靠靠靠靠靠靠靠靠靠靠靠靠靠靠靠靠靠靠靠靠靠靠靠靠靠靠靠靠靠</em></strong></p><p><br></p><p><strong><em>付款的时间浪费空间克隆证据</em></strong></p>'
		}
	}
</script>

<style>
	
</style>
