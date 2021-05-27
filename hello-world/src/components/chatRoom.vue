<template>
  <div id='chatroom'>
    <div class='header'>
      <h4 class="header-text">ChatRoom:{{roomID}}</h4>
    </div>
    <div class='body'>
      <div v-for="(item,index) in msgs" :key="index">
                <div v-if="item.msgType=='online'" class="onlineMsg">
                    <div class="sysTime">{{item.time}}</div>
                    <div class="online">{{item.username}}上线</div>
                </div>
                <div v-else-if="item.msgType=='offline'" class="offlineMsg">
                    <div class="sysTime">{{item.time}}</div>
                    <div class="online">{{item.username}}下线</div>
                </div>
                <div v-else-if="item.msgType=='clientMsg'" class="clientMsg">
                    <div class="sysTime">{{item.time}}</div>
                    <div v-if="item.username==JSON.parse($route.query.information).id" class="self">
                      
                        <div class="bubble">
                            <div class="chatBubble">{{item.msg}}</div>
                            <div class="triangle"></div>
                        </div>
                        <div class="user">{{item.username}}</div>
                    </div>
                    <div v-else class="others">
                        <div class="user">{{item.username}}</div>
                        <div class="bubble">
                            <div class="chatBubble">{{item.msg}}</div>
                            <div class="triangle"></div>
                        </div>
                    </div>
                </div>
            </div>
            
    </div>
    <div class='msgInput'>
                <input
          v-model='msg'
          autofocus
          class='input'
          type='text'
          placeholder='发送信息'
          @keydown.enter="send(msg)"
        />
      </div>
  </div>
</template>

<script>
import socketio from 'socket.io-client';
import storage from '../../server/storage';

const moment = require('moment');

export default {
  name: 'chatRoom',
  data() {
    return {
      socket: null,
      msg: '',
      msgs: storage.fetch(),
      roomID: '0',
      msgID: {},
    };
  },
  mounted() {
    this.socket = socketio('http://localhost:8081');
    var information = JSON.parse(this.$route.query.information);
    this.roomID = 'roomID 123';
    const IDdata = {
      roomID: 'this.roomID',
      username: information.id,
    };
    if (this.roomID && information.id) {
      this.socket.emit('joinRoom', IDdata);
    } else {
      this.$router.push('/');
    }
    this.socket.on('online', (data) => {
      this.msgs.push({
        msgType: 'online',
        username: data,
        time: moment().format('HH:mm:ss'),
      });
      storage.save(this.msgs);
    });
    this.socket.on('broadcastMsg', (data) => {
      this.msgs.push({
        msgType: 'clientMsg',
        username: data.username,
        msg: data.msg,
        time: moment().format('HH:mm:ss'),
      });
      storage.save(this.msgs);
    });
    this.socket.on('offline', (data) => {
      this.msgs.push({
        msgType: 'offline',
        username: data,
        time: moment().format('HH:mm:ss'),
      });
      storage.save(this.msgs);
    });
  },
  updated() {
    this.$nextTick(() => {
      const oBody = document.querySelector('.body');
      oBody.scrollTop = oBody.scrollHeight;
    });
  },
  methods: {
      send(data) {
        var information = JSON.parse(this.$route.query.information);
      const transdata = {
        msg: data,
        username: information.id,
      };
      if (data) {
        this.socket.emit('msg', transdata);
        this.msg = '';
      }
    },
  },
};
</script>

<style scoped>
a {
  text-decoration: none;
}
a:hover {
  color: brown;
}
.chatroom {
  width: 400px;
  height: 600px;
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
.header-text{
  margin:0 auto;
}
.body {
  height: 300px;
  width: 100%;
  overflow: auto;
  text-align: center;
}
.iconfont {
  font-size: 24px;
}
.logout,
.about {
  padding: 7px;
}
.sysTime {
  color: #999;
  font-size: 13px;
  margin-bottom: 3px;
}
.onlineMsg,
.offlineMsg,
.clientMsg {
  margin-bottom: 10px;
  height: 50px;
  width: 100%;
}
.clientMsg {
  position: relative;
}
.online,
.offline {
  display: inline-block;
  height: 23px;
  padding-left: 10px;
  padding-right: 10px;
  border-radius: 3px;
  color: #999;
  text-align: center;
  line-height: 23px;
  background-color: rgb(209, 209, 209);
  font-size: 16px;
  box-sizing: border-box;
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
.footer {
  height: 45px;
  width: 100%;
  position: absolute;
  bottom: 0;
  display: -webkit-flex;
  display: flex;
}
.fade-enter-active,
.fade-leave-active {
  transition: opacity 0.5s;
}
.fade-enter,
.fade-leave-to {
  opacity: 0;
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
  padding-left: 50px;
  background-color: rgb(227, 228, 231);
  text-align: center;
  font-size: 18px;
  caret-color: rgb(62, 141, 231);
  color: rgb(55, 125, 182);
}
</style>
