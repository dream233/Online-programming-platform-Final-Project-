# 如何优美的运行这个项目
## 0.一键安装依赖（首先需要进入项目文件夹）
```
install.bat
```
## 1.安装依赖项目


### Project setup（基本组件）
```
npm install
```

### router install（跳转支持）

```
npm install vue-router --save
```

### element-ui install(UI支持)

```
npm i element-ui -S
```

### axios(前后端交互)
```
npm install axios --save
```

### codemirror install（代码框支持）
```
npm install --save codemirror
npm install --save dedent
```


### editor（面试题目支持）
```
npm install quill --save
npm install vue-quill-editor --save

npm install quill-image-resize-module -S
下面这两个我创建项目的时候好像就有了所以我没弄，如果你们报错了可以试一试
npm install node-sass --save-dev
npm install sass-loader --save-dev
如果还要npm别的，可以根据提示或者问问我，我记得是不用了
```

### socketio（聊天室支持）
```
npm install --save moment

npm i socket.io --save

npm i vue-socket.io --save

npm i socket.io-client --save
```

# 2.运行项目

## 2.1 运行 socketio
```
npm run server
```
## 2.2 新开一个终端   Compiles and hot-reloads for development
```
npm run serve
```

### Compiles and minifies for production
```
npm run build
```

## Customize configuration
See [Configuration Reference](https://cli.vuejs.org/config/).


