from flask import Flask, render_template, request
from flask_socketio import SocketIO, emit, disconnect, join_room, leave_room


app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'

# 跨域问题是真的坑
socketio = SocketIO(app, cors_allowed_origins='*')

room_list = {}
@socketio.on('joinRoom')
def on_join(data):
    print(data)
    username = data['username']
    room = data['roomID']
    join_room(room)

    print('username: '+username+', 加入 '+room+' 房间!')

@socketio.on('msg')
def on_msg(data):
    username = data['username']
    userid = data['id']
    msg = data['msg']
    emit('broadcastMsg', data, broadcast=True)
    print('username: ' + username + 'userid: ' + userid + '发送的消息是' + msg)


if __name__ == '__main__':
    socketio.run(app, port='8081')