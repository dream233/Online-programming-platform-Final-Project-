<template>
  <div id="app">
	  <title1></title1>
	  <router-view></router-view>
  </div>
</template>

<script>
	import title1 from './components/title1.vue'
	import Vue from 'vue'
	export default{
		data(){
			return{
				name:String
			}
		},
		methods:{
			
		},
		components:{
			title1
		}
	}
</script>

<style>
	
</style>