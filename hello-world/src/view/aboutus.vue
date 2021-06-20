<template>
  <div class="block">
	<!-- <span class="demonstration">默认 Hover 指示器触发</span> -->
	
	<div style="width:50%;margin:auto">
	<el-carousel>
		<el-carousel-item v-for="item in imglist" :key="item.id">
			<el-image :src="item.img" class="small" ></el-image>		
		</el-carousel-item>
	</el-carousel>
    </div>
	
	<el-collapse v-model="activeNames" @change="handleChange">
		<el-collapse-item title="网站框架及服务器" name="1">
			<div>整体框架编写：谭笑衡</div>
			<div>网站参数传递设计：谭笑衡</div>
			<div>导航栏设计：谭笑衡</div>
			<div>服务器维护，项目部署：梁家榕</div>
			<div>服务器数据库：蒋宇涛</div>
		</el-collapse-item>
		
		<el-collapse-item title="登录注册模块" name="2">
			<div>模块功能介绍：支持邮箱登录和注册</div>
			<div>前端：谭笑衡</div>
			<div>后端：蒋宇涛，袁志琛</div>
		</el-collapse-item>

		<el-collapse-item title="面试题模块" name="3">
			<div>模块功能介绍：面试官可填写面试题，每个面试题有固定链接（可以通过题目id方式访问），支持新建面试题和修改面试题目，支持邀请一个候选人编程（通过加入指定的面试房间），面试题目支持富文本格式</div>
			<div>前端：谭笑衡</div>
			<div>后端：蒋宇涛，袁志琛</div>
		</el-collapse-item>

		<el-collapse-item title="在线编程模块" name="4">
			<div>模块功能介绍：候选人可在线编写代码，代码支持多种语言高亮，候选人侧提交最终编程代码，面试官侧刷新能看到最终代码</div>
			<div>前端：梁家榕</div>
			<div>后端：蒋宇涛，袁志琛，梁家榕</div>
		</el-collapse-item>
		
		<el-collapse-item title="在线留言模块" name="5">
			<div>模块功能介绍：候选人可以通过文字给面试官留言，面试官可以回复，留言内容长期保存，留言模块自动刷新</div>
			<div>前端框架：莫文仪</div>
			<div>前端实时文字聊天模块中页面内容渲染的实现：谭笑衡，莫文仪</div>
			<div>前后端socketio传递消息：梁家榕，莫文仪</div>
			<div>后端房间号处理：蒋宇涛，袁志琛</div>
			<div>后端聊天信息处理：梁家榕</div>
		</el-collapse-item>
		
		<el-collapse-item title="挑战1:在线编程模块支持自动刷新" name="6">
			<div>模块功能介绍：候选人侧代码支持自动保存，面试官侧代码自动刷新</div>
			<div>前端：梁家榕</div>
			<div>后端：蒋宇涛，袁志琛，梁家榕</div>
		</el-collapse-item>
		
		<el-collapse-item title="挑战2:在线留言模块改成实时文字聊天" name="7">
			<div>模块功能介绍：候选人和面试官可实时文字聊天，其他获得链接的人都可参与文字聊天</div>
			<div>前端框架：莫文仪</div>
			<div>前端实时文字聊天模块中页面内容渲染的实现：谭笑衡，莫文仪</div>
			<div>前后端socketio传递消息：梁家榕，莫文仪</div>
			<div>后端房间号处理：蒋宇涛，袁志琛</div>
			<div>后端聊天信息处理：梁家榕</div>
		</el-collapse-item>
		
		<el-collapse-item title="挑战4:在线编程模块支持运行 JS 代码" name="8">
			<div>模块功能介绍：候选人和面试官可在线运行 JS 代码并查看输出</div>
			<div>前端：袁志琛</div>
			<div>后端：袁志琛</div>
		</el-collapse-item>
		
		<el-collapse-item title="挑战5:在线编程模块支持协同编辑" name="9">
			<div>模块功能介绍：候选人和面试官可实时协作编程</div>
			<div>前端：梁家榕</div>
			<div>后端：蒋宇涛，袁志琛，梁家榕</div>
		</el-collapse-item>
	</el-collapse>
	
  </div>
</template>
<script>
  export default {
    data() {
      return {
        activeName: '1',
		imglist:[
			{id:1,img:require('../../assets/main.png')},
			{id:2,img:require('../../assets/joinroom.png')},
			{id:3,img:require('../../assets/code.png')},
			{id:4,img:require('../../assets/problem.png')},
		],
      };
    }
  }
</script>



<style>
  .el-carousel__item h3 {
    color: #475669;
    font-size: 14px;
    opacity: 0.75;
    line-height: 150px;
    margin: 0;
  }

  .el-carousel__item:nth-child(2n) {
     background-color: #99a9bf;
  }
  
  .el-carousel__item:nth-child(2n+1) {
     background-color: #d3dce6;
  }
</style>