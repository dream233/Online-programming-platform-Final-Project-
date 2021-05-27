<template>
	<div>
		<title1></title1>
		<router-view></router-view>
		<button @click="test()">点击查看登陆信息</button>
	</div>
	
</template>

<script>
	import title1 from '../components/title1.vue'
	export default {
	    
		components: {
			title1
		},
		methods: {
			test(){
				var information = JSON.parse(this.$route.query.information);
				alert('这里是用户'+information.name+'的首页');
			}
		}
	  }
</script>

<style>
</style>
