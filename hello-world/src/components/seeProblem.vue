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
	  // Quill.register('modules/imageDrop', ImageDrop)
	  Quill.register('modules/imageResize', ImageResize)
	export default{
		data(){
			return{
				message: '<p>题目未响应，信息有误！</p>'
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
			if(this.$route.params.password=='1'){
				this.message='<ul><li><strong><em><u>dkfjlskdjfkslf</u></em></strong></li><li><strong><em><u>附件是立刻搭街坊立刻是</u></em></strong></li><li><strong><em><u>是独立开发炯之女会计出纳在</u></em></strong></li><li><strong><em><u>法律搭街坊立刻就在芬兰空军的离开这世界</u></em></strong></li></ul><p><strong><em><u>dk附件是的JFK老师的</u></em></strong></p><p><br></p><p><br></p><p><br></p><p><strong><em><u>首都基辅罗斯大家来看</u></em></strong></p><p><strong><em><u>搭街坊昆仑山觉得</u></em></strong></p><p><br></p><p><br></p><p><br></p><p><br></p><p><br></p><p><br></p><p><br></p><p><br></p><p><strong><em><u>打卡时间分厘卡圣诞节饭卡里说的你看     方式决定离开房间昆仑山大家</u></em></strong></p><p><strong><em>但是看了方式</em></strong></p><p><br></p><p><br></p><p><br></p><p><strong><em>出行距离空间kl</em></strong></p><p><br></p><p><strong><em>发就可怜见立刻就 JFK四点零分记录卡撒旦解放开始JFK老师讲课靠靠靠靠靠靠靠靠靠靠靠靠靠靠靠靠靠靠靠靠靠靠靠靠靠靠靠靠靠靠靠靠靠靠靠靠靠靠</em></strong></p><p><br></p><p><strong><em>付款的时间浪费空间克隆证据</em></strong></p>'
			}
		}
	}
</script>

<style>
</style>
