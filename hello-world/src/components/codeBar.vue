<template>
	<div>
		<codemirror v-model="code" :options="cmOption" />
		<!-- <button @click="getMessage()">get</button>
		<button @click="postMessage()">post</button>
		<el-input v-model="input" placeholder="请输入内容"></el-input> -->
	</div>
	
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
`import someResource from 'codemirror/some-resource'
export default {
data () {
  // 这是一个包含、代码提示、折叠、选中、sublime模式...的编辑器
  // 按下Ctrl键可以体验代码提示
  // 可以尝试sublime下的快捷键操作
  return {
	exampleCode: 'const a = 10',
	cmOption: {
	  tabSize: 4,
	  styleActiveLine: true,
	  lineNumbers: true,
	  line: true,
	  mode: 'text/javascript',
	  lineWrapping: true,
	  theme: 'default'
	}
  }
},
components: examples
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
          // hint.js options
          hintOptions:{
            // 当匹配只有一项的时候是否自动补全
            completeSingle: false
          },
          //快捷键 可提供三种模式 sublime、emacs、vim
          keyMap: "sublime",
          matchBrackets: true,
          showCursorWhenSelecting: true,
          theme: "monokai",
          extraKeys: { "Ctrl": "autocomplete" }
        },
		input:'dasda'
      }
	  
    },
	
	methods: {
		
	    getMessage() {
	      const path = this.global.baseURL + ':5000/postcode';
		  // console.log("get function")
		  var i = JSON.parse(this.$route.query.information);
		  var room = i.roomID;
		  var information ={
		  	sendRoom:room,
		  	type:'get'
		  }
		  
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
			// console.log(information)
		    axios.post(path,information)
			.then((res) => {
				console.log(res.data);
		    })
		    .catch((error) => {
		      // eslint-disable-next-line
		      console.error(error);
			});
		},
	},
	
	mounted() {
		if(this.timer){
			clearInterval(this.timer)
		}else{
			this.timer = setInterval(()=> {
				this.postMessage();
			    this.getMessage();	
			}, 5000);
		}
	},
	
	
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
</style>