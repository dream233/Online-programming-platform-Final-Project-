from werkzeug import debug
from database import match_user
from flask import Flask, jsonify
from flask_cors import CORS
from uuid import uuid1

from database import *
from interface import *
from email_sender import send_email

from flask_socketio import SocketIO, emit, disconnect, join_room, leave_room

app = Flask(__name__)
app.config.from_object(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app, cors_allowed_origins='*')

# enable CORS
CORS(app, supports_credentials=True)
reg_queue = {}

def user_in_reg_queue(email)->bool:
    for it in reg_queue.values():
        if it.get('email',0) == email:
            return True
    return False

# 注册
@app.route('/register',methods=['POST','GET'])
def register():
    uinfo = get_reg_info()        # 获取登陆信息
    resp = {'status': 'success'}
    if not uinfo:                   # 如果用户信息不全面，直接报错
        resp['error'] = '用户信息错误'
        resp['message'] = 'N'
        return jsonify(resp)
    
    email = uinfo['email']
    if (not have_user(email)) and (not user_in_reg_queue(email)):        # 判断用户名称是否已经存在
        uid = uuid1().hex
        reg_queue[uid] = uinfo
        url = "111.229.68.117:5000/regcheck/"+uid
        resp['message'] = 'Y'
        if send_email(url,email):      # 发送验证邮件
            resp['message'] = 'Y'
        else:
            resp['message'] = 'N'
            resp['error'] = "服务器错误"
    else:
        resp['message'] = 'N'
        resp['error'] = '用户已经存在'
    return jsonify(resp)

# 邮箱验证
@app.route('/regcheck/<uuid>')
def reg_check(uuid:str):
    if uuid not in reg_queue:
        return "验证失败"
    uinfo =  reg_queue.get(uuid)
    if create_user(uinfo):
        reg_queue.pop(uuid)
        return "验证成功"
    else:
        return "服务器错误！"

# 登陆    
@app.route('/login',methods=['POST','GET'])
def login():
    uinfo = get_login_info()
    resp = {'status': 'success'}
    if not uinfo:                   # 如果用户信息不全面则返回错误
        resp['error'] = '用户信息错误'
        resp['message'] = 'N'
        return jsonify(resp)
    
    # 能否查询到这个用户的信息
    user_info = match_user(uinfo['email'],uinfo['password'],uinfo['usertype'])
    if not user_info:
        resp['message'] = 'N'
        resp['error'] = "服务器错误"
    else:
        resp['message'] = 'Y'
        resp['username'] = user_info['username']        # 登陆成功还返回用户名称
    
    return jsonify(resp)

# 获取题目信息
@app.route('/problemCheck', methods=['GET','POST'])
def problemCheck():
    problem_req = get_req_of_problem()
    resp = {'status': 'success'}
    if not problem_req:             # 请求信息不全返回报错
        resp['error'] = "题目信息错误"
        resp['message'] = 'N'
        return jsonify(resp)

    prob_info = get_problem(problem_req['id'])
    if not prob_info:
        resp['message'] = 'N'
    else:
        resp['message'] = 'Y'
        resp['password'] = prob_info['password']
        resp['owner'] = prob_info['owner']
        resp['contents'] = prob_info['contents']
    
    return jsonify(resp)

# 显示题目列表
@app.route('/pblist', methods=['POST','GET'])
def list_problem():
    resp = {'status': 'success'}
    pblist = list_problemid()

    if pblist is not None:
        resp['pblist'] = pblist
    else:
        resp['pblist'] = []
        resp['error'] = "服务器错误"
    
    return jsonify(resp)

# 创建题目
@app.route('/problemCreate', methods=['GET','POST'])
def problem_create():
    resp = {'status': 'success'}
    prob_info = get_problem_info()
    if create_problem(prob_info):
        resp['message'] = 'Y'
    else:
        resp['message'] = 'N'
    return jsonify(resp)

# 修改题目
@app.route('/problemEdit', methods=['GET','POST'])
def problem_edit():
    resp = {'status': 'success'}
    prob_info = get_problem_info()
    if alter_problem(prob_info['ProblemID'],prob_info):
        resp['message'] = 'Y'
    else:
        resp['message'] = 'N'
    return jsonify(resp)

# 发送接收面试代码
code_list = {}
@app.route('/postcode', methods=['POST','GET'])
def post_code():
    data = get_code_info()
    if data['type'] == 'get':           # get表示请求代码
        if data.get('sendRoom',False):
            code = code_list[data.get('sendRoom')]
        else:
            code = "wrong roomNum"
        return code
    elif data['type'] == 'post':        # post表示提交代码
        if data.get('sendRoom',False):
            code_list[data.get('sendRoom')] = data.get('sendCode','')
            return "sucess"
    return "error"

# 创建房间，获取历史记录
@app.route('/createroom', methods=['GET','POST'])
def createroom():
    resp = {'status': 'success'}
    data = get_room_info()
    roomid = data['roomid']
    if not have_chatroom(roomid):
        create_chatroom(roomid)
        resp['message'] = 'N'
    else:
        history = get_comment(roomid)
        resp['message'] = 'Y'
        resp['chathistory'] = history
    return jsonify(resp)

# 加入房间，获取历史记录
@app.route('/joinroom',methods=['GET','POST'])
def joinroom():
    resp = {'status': 'success'}
    data = get_room_info()
    roomid = data['roomid']
    if not have_chatroom(roomid):
        resp['message'] = 'N'
    else:
        history = get_comment(roomid)
        resp['message'] = 'Y'
        resp['chathistory'] = history
    return jsonify(resp)

# 添加聊天记录
@app.route('/chat', methods=['GET','POST'])
def add_history():
    resp = {'status': 'success'}
    data = get_chat_info()
    if add_comment(data):
        return jsonify(resp)
    else:
        return jsonify({'status': 'error'})

# 在线聊天系统
# 加入房间
@socketio.on('joinRoom')
def on_join(data):
    room = data['roomID']
    join_room(room)

    print(data)

# 发送信息
@socketio.on('msg')
def on_msg(data):
    pkg = {'username':data['email'],'contents':data['msg'],'roomid':data['roomID']}
    add_comment(pkg)
    emit('broadcastMsg', data, broadcast=True)

    print(data)

if __name__=='__main__':
    socketio.run(app, port=5000,debug=True, host='0.0.0.0')
    