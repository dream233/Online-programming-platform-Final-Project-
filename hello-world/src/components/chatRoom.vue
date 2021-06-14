<template>
  <div id="chatroom" class="chat">
    <div class="header">
      <h4 class="header-text">ChatRoom:{{ roomID }}</h4>
    </div>
    <div class="body">
      <!-- 记录 -->
      <div v-for="(item, ind) in history" :key="ind">
        <div class="clientMsg">
          <div class="sysTime">{{ item.time }}</div>

          <div
            v-if="item.email == JSON.parse($route.query.information).name"
            class="self"
          >
            <div class="bubble">
              <div class="chatBubble">{{ item.msg }}</div>
              <div class="triangle"></div>
            </div>
            <div class="user">{{ item.email }}</div>
          </div>
          <div v-else class="others">
            <div class="user">{{ item.email }}</div>
            <div class="bubble">
              <div class="chatBubble">{{ item.msg }}</div>
              <div class="triangle"></div>
            </div>
          </div>
        </div>
      </div>
    </div>
    <!--发送内容-->
    <div class="beforeInput"></div>
    <div class="msgInput">
      <textarea
        v-model="msg"
        autofocus
        class="input"
        type="text"
        placeholder="请输入会话内容"
        @keydown.enter="send(msg)"
        maxlength="20"
      />
      <button class="sendBtn" id="serviceSendBtn">Enter</button>
    </div>
  </div>
</template>

<script>
import socketio from "socket.io-client";
import storage from "../api/storage";
import axios from "axios";

const moment = require("moment");

export default {
  name: "chatRoom",
  data() {
    return {
      socket: null,
      msg: "",
      msgs: storage.fetch(),
      roomID: "0",
      msgID: {},
      history: storage.fetch(),
    };
  },
  // 创建
  created() {
    this.socket = socketio(this.global.baseURL + ":5000");
    var information = JSON.parse(this.$route.query.information);
    this.roomID = information.roomID;
    const IDdata = {
      roomID: this.roomID,
      username: information.username,
    };
    var x = {
      roomID: information.roomID,
    };
    var that = this;
    const path = "http://111.229.68.117:5000/joinroom";
    axios
      .post(path, x)
      .then((res) => {
        // 发送roomID给后端，获取聊天记录
        this.history = res.data.chathistory;
        that.history = res.data.chathistory;
      })
      .catch((error) => {
        console.log(error);
      });

    console.log(this);
    // 成功进入房间，调用joinRoom
    if (this.roomID && information.id) {
      this.socket.emit("joinRoom", IDdata);
    } else {
      this.$router.push("/");
    }

    // 监听服务器回传的信息
    this.socket.on("broadcastMsg", (data) => {
      this.history.push({
        msgType: "clientMsg",
        email: data.email,
        msg: data.msg,
        time: moment().format("HH:mm:ss"),
      });

      storage.save(this.history);
    });
  },

  // 重新调用DOM时，回到聊天室最上方
  updated() {
    this.$nextTick(() => {
      const oBody = document.querySelector(".body");
      oBody.scrollTop = oBody.scrollHeight;
    });
  },

  methods: {
    send(data) {
      var information = JSON.parse(this.$route.query.information);
      const transdata = {
        msg: data,
        email: information.name,
        roomID: this.roomID
      };
      if (data) {
        this.socket.emit("msg", transdata);
        this.msg = "";
      }
    },
  },
};
</script>

<style scoped>
.sendBtn {
  width: 68px;
  height: 25px;
  background: #62aaec;
  border: none;
  position: absolute;
  bottom: 10px;
  right: 10px;
  color: white;
}
input:focus,
textarea:focus {
  outline: none;
}
.chatroom {
  position: relative;
  border: 1px solid #999;
  margin: 0 auto;
  margin-top: 15px;
}
.header {
  background-color: #6a8396;
  height: 50px;
  display: -webkit-flex;
  display: flex;
  justify-content: space-between;
  align-items: center;
}
.header-text {
  margin: 0 auto;
}
.body {
  height: 320px;
  width: 100%;
  overflow: auto;
  text-align: center;
}

.clientMsg {
  margin-bottom: 10px;
  height: 50px;
  width: 100%;
  position: relative;
}

.self {
  position: absolute;
  right: 14px;
}
.others {
  position: absolute;
  left: 14px;
}
.bubble {
  display: inline-block;
  position: relative;
}
.chatBubble {
  height: 30px;
  line-height: 30px;
  background-color: rgb(198, 205, 243);
  font-size: 16px;
  color: rgb(58, 58, 58);
  border-radius: 10px;
  padding-left: 10px;
  padding-right: 10px;
}
.self .triangle {
  position: absolute;
  right: -10px;
  top: 10px;
  border-left: 10px solid rgb(198, 205, 243);
  border-bottom: 10px solid transparent;
}
.others .triangle {
  position: absolute;
  left: -10px;
  top: 10px;
  border-right: 10px solid rgb(198, 205, 243);
  border-bottom: 10px solid transparent;
}
.self .user {
  display: inline-block;
  margin-left: 10px;
}
.others .user {
  display: inline-block;
  margin-right: 10px;
}

.sysTime {
  color: #999;
  font-size: 13px;
  margin-bottom: 3px;
}
.beforeInput {
  position: relative;
  width: 100%;
  height: 5px;
  background-color: rgb(246, 247, 250);
}
.msgInput {
  position: relative;
  width: 100%;
  height: 200px;
}
.msgInput .input {
  box-sizing: border-box;
  width: 100%;
  height: 200px;
  border: 1px solid #eee;
  font-family: normal;
  padding: 15px;
  background-color: rgb(246, 247, 250);
  font-size: 16px;
  caret-color: rgb(62, 141, 231);
  color: rgb(55, 125, 182);
}
</style>