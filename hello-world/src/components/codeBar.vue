<template>
	<div>
		<codemirror v-model="code" :options="cmOption" />
		<button @click="compilejs()">运行代码</button>
		<!-- <button @click="getMessage()">get</button>
		<button @click="postMessage()">post</button>
		<el-input v-model="input" placeholder="请输入内容"></el-input> -->
	</div>
	<!-- 按钮 -->

	

	
</template>

<script>
  import dedent from 'dedent'
  import { codemirror } from 'vue-codemirror'
  // language
  import 'codemirror/mode/javascript/javascript.js'
  // theme css
  import 'codemirror/theme/monokai.css'
  // require active-line.js
  import'codemirror/addon/selection/active-line.js'
  // styleSelectedText
  import'codemirror/addon/selection/mark-selection.js'
  import'codemirror/addon/search/searchcursor.js'
  // hint
  import'codemirror/addon/hint/show-hint.js'
  import'codemirror/addon/hint/show-hint.css'
  import'codemirror/addon/hint/javascript-hint.js'
  import'codemirror/addon/selection/active-line.js'
  // highlightSelectionMatches
  import'codemirror/addon/scroll/annotatescrollbar.js'
  import'codemirror/addon/search/matchesonscrollbar.js'
  import'codemirror/addon/search/searchcursor.js'
  import'codemirror/addon/search/match-highlighter.js'
  // keyMap
  import'codemirror/mode/clike/clike.js'
  import'codemirror/addon/edit/matchbrackets.js'
  import'codemirror/addon/comment/comment.js'
  import'codemirror/addon/dialog/dialog.js'
  import'codemirror/addon/dialog/dialog.css'
  import'codemirror/addon/search/searchcursor.js'
  import'codemirror/addon/search/search.js'
  import'codemirror/keymap/sublime.js'
  // foldGutter
  import'codemirror/addon/fold/foldgutter.css'
  import'codemirror/addon/fold/brace-fold.js'
  import'codemirror/addon/fold/comment-fold.js'
  import'codemirror/addon/fold/foldcode.js'
  import'codemirror/addon/fold/foldgutter.js'
  import'codemirror/addon/fold/indent-fold.js'
  import'codemirror/addon/fold/markdown-fold.js'
  import'codemirror/addon/fold/xml-fold.js'
  // let CodeMirror = require('codemirror/lib/codemirror')
  
  import axios from 'axios'
  import qs from 'qs'
  
  export default {
    name: 'codemirror-example-javascript',
    title: 'Mode: text/javascript & Theme: monokai',
    components: {
      codemirror
    },
    data() {
      return {
		  
		code: 
`function main(){
  function a(x,y){
    return x+y;
  } 
  return a(1,2);
}
`,
        cmOption: {
          tabSize: 4,
          styleActiveLine: false,
          lineNumbers: true,
          styleSelectedText: false,
          line: true,
          foldGutter: true,
          gutters: ["CodeMirror-linenumbers", "CodeMirror-foldgutter"],
          highlightSelectionMatches: { showToken: /\w/, annotateScrollbar: true },
          mode: 'text/javascript',
		  // resetSelectionOnContextMenu:false,
          // hint.js options
          hintOptions:{
            // Whether to autocomplete when there is only one match
            completeSingle: false
          },
          //Shortcut keys can provide three modes: sublime、emacs、vim
          keyMap: "sublime",
          matchBrackets: true,
          showCursorWhenSelecting: true,
          theme: "monokai",
          extraKeys: { "Ctrl": "autocomplete" }
        },
		
		input:'dasda',
		codeLength:0,
		
      }
	  
    },
	// computed: {
	//     codemirror() {
	//       return this.$refs.myCm.codemirror
	//     }
	//   },
	
	methods: {
		
	    getMessage() {
		  // console.log(this.codemirror.getCursor())
	      const path = this.global.baseURL + ':5000/postcode';
		  // console.log("get function")
		  var i = JSON.parse(this.$route.query.information);
		  var room = i.roomID;
		  var information ={
		  	sendRoom:room,
		  	type:'get'
		  }
		  
		  // console.log("in get");
	      axios.post(path,information)
	        .then((res) => {
	          this.code = res.data;
	        })
	        .catch((error) => {
	          // eslint-disable-next-line
	          console.error(error);
			});
		},
		
		postMessage() {
			
			// console.log("in post");
		    const path = this.global.baseURL + ':5000/postcode';
			// console.log("post function")
			var i = JSON.parse(this.$route.query.information);
			var room = i.roomID;
			// console.log('room id is'+ room)
			var information ={
				sendCode:this.code,
				sendRoom:room,
				type:'post'
			}
			this.codeLength = this.code.length
			// console.log(information)
		    axios.post(path,information)
			.then((res) => {
				// console.log(res.data);
		    })
		    .catch((error) => {
		      // eslint-disable-next-line
		      console.error(error);
			});
		},
		compilejs(){
			const path = this.global.baseURL + ':5000/compilejs';
			var i = JSON.parse(this.$route.query.information);
			var room = i.roomID;
			var information ={
				sendCode:this.code,
				sendRoom:room,
				type:'post'
			}
			axios.post(path,information)
			.then((res)=>{
				alert('function return: ' + res.data.answer);
			})
			.catch((error) => {
			  // eslint-disable-next-line
			  console.error(error);
			});
		},
		
		checkLength(){
			// console.log(' last is ' + this.codeLength + ' now is ' + this.code.length);
			if(this.codeLength != this.code.length)
			{
				this.postMessage();
				setTimeout(this.postMessage(),200);
			}
		},
		
	
	},
	mounted() {
			if(this.timer){
				clearInterval(this.timer)
			}else{
				this.timer = setInterval(()=> {
					this.checkLength();
				}, 1000);
				this.timer = setInterval(()=> {
				    this.getMessage();	
				}, 5000);
			}
		},
	
	created(){
		this.getMessage()
	},
	destroyed() {
		// Clear the timer every time you leave the current interface
		clearInterval(this.timer)
		this.timer = null
	}
	
	
	
}
</script>

<style>
  .CodeMirror-focused .cm-matchhighlight {
    background-image: url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAIAAAACCAYAAABytg0kAAAAFklEQVQI12NgYGBgkKzc8x9CMDAwAAAmhwSbidEoSQAAAABJRU5ErkJggg==);
    background-position: bottom;
    background-repeat: repeat-x;
  }
  .cm-matchhighlight {
    background-color: lightgreen;
  }
  .CodeMirror-selection-highlight-scrollbar {
    background-color: green;
  }
  .CodeMirror {
	  border: 1px solid #eee;
	  height: 500px !important;
  }

  .CodeMirror-scroll {
	  height: 500px;
	  overflow-y: hidden;
	  overflow-x: auto;
  }
</style>