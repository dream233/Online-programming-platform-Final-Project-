from flask import Flask, jsonify, session
from flask_cors import CORS
from uuid import uuid1
from flask_socketio import SocketIO, emit, join_room
import execjs
from database import *
from interface import *
from email_sender import *

app = Flask(__name__)
app.config.from_object(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app, cors_allowed_origins='*')

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})
CORS(app, supports_credentials=True)

##############################################################################
# Login/Sign Module
##############################################################################

# register queue
reg_queue = {}
def user_in_reg_queue(email)->bool:
    for it in reg_queue.values():
        if it.get('email',0) == email:
            return True
    return False

# register
@app.route('/register',methods=['POST','GET'])
def register():
    uinfo = get_reg_info()        # 获取登陆信息
    resp = {'status': 'success'}
    if not uinfo:                   # 如果用户信息不全面，直接报错
        resp['error'] = '用户信息错误'
        resp['message'] = 'N'
        return jsonify(resp)
    
    email = uinfo['email']
    # print(not have_user(email))
    # print(not user_in_reg_queue(email))
    if (not have_user(email)) and (not user_in_reg_queue(email)):        # 判断用户名称是否已经存在
        uid = uuid1().hex
        url = "http://127.0.0.1:5000/regcheck/"+uid
        if send_reg_email(url,email):      # 发送验证邮件
            reg_queue[uid] = uinfo
            resp['message'] = 'Y'
        else:
            resp['message'] = 'N'
            resp['error'] = "服务器错误"
    else:
        resp['message'] = 'N'
        resp['error'] = '用户已经存在'
    return jsonify(resp)

# email verification
@app.route('/regcheck/<uuid>')
def reg_check(uuid:str):
    if uuid not in reg_queue:       # 不存在此链接，验证失败
        return "验证失败"
    uinfo =  reg_queue.get(uuid)
    if create_user(uinfo):          # 创建用户
        reg_queue.pop(uuid)
        return "验证成功"
    else:
        return "服务器错误！"

# forget psd
@app.route('/forgetpassword',methods=['POST','GET'])
def forget_password():
    data = request.get_json()
    print(data)
    email = data.get('email',False)
    resp = {'status': 'success'}
    if email:                               # 判断邮箱是否合法
        user_info = get_user_info(email)
        if user_info:                       # 判断邮箱是否存在
            password = user_info['password']
            send_forgetpwd_email(password,email)
            resp['message']= 'Y'
        else:
            resp['message']= 'N'
    else:
        resp['message']= 'N'
    
    return jsonify(resp)

# login
@app.route('/login',methods=['POST','GET'])
def login():
    uinfo = get_login_info()
    # print(uinfo)
    resp = {'status': 'success'}
    if not uinfo:                   # 如果用户信息不全面则返回错误
        resp['error'] = '用户信息错误'
        resp['message'] = 'N'
        return jsonify(resp)
    
    # 查询用户信息,并进行匹配
    user_info = get_user_info(uinfo['email'])
    if not user_info:
        resp['message'] = 'N'
        resp['error'] = "用户不存在"
    elif uinfo['password'] == user_info.get('password','') and uinfo['usertype'] == user_info.get('type',''):
        resp['message'] = 'Y'
        resp['username'] = user_info['username']        # 登陆成功返回用户名称
        session['username'] = user_info['username']
    else:
        resp['message'] = 'N'
        resp['error'] = "用户不匹配"
    
    return jsonify(resp)

##############################################################################
# Question Management
##############################################################################

# display problem content
@app.route('/problemCheck', methods=['GET','POST'])
def problemCheck():
    problem_req = request.get_json()
    resp = {'status': 'success'}
    if not problem_req:             # 请求信息不全返回报错
        resp['error'] = "题目信息错误"
        resp['message'] = 'N'
        return jsonify(resp)

    prob_info = get_problem(problem_req['id'])  # 按ID获取题目信息
    
    if not prob_info:
        resp['message'] = 'N'
    else:
        resp['message'] = 'Y'
        resp['password'] = prob_info['password']
        resp['owner'] = prob_info['owner']
        resp['contents'] = prob_info['contents']
    
    return jsonify(resp)

# display problem list
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

# create problem
@app.route('/problemCreate', methods=['GET','POST'])
def problem_create():
    resp = {'status': 'success'}
    prob_info = request.get_json()
    if create_problem(prob_info):
        resp['message'] = 'Y'
    else:
        resp['message'] = 'N'
    return jsonify(resp)

# edit problem
@app.route('/problemEdit', methods=['GET','POST'])
def problem_edit():
    resp = {'status': 'success'}
    prob_info = request.get_json()
    if alter_problem(prob_info['ProblemID'],prob_info):
        resp['message'] = 'Y'
    else:
        resp['message'] = 'N'
    return jsonify(resp)

##############################################################################
# Interview Code Processing
##############################################################################

# 发送接收面试代码
code_list = {}
@app.route('/postcode', methods=['POST','GET'])
def post_code():
    data = get_code_info()
    if data['type'] == 'get':           # get表示请求代码
        if data.get('sendRoom',False):
            code = code_list.get(data.get('sendRoom'),'')
        else:
            code = "wrong roomNum"
        return code
    elif data['type'] == 'post':        # post表示提交代码
        if data.get('sendRoom',False):
            code_list[data.get('sendRoom')] = data.get('sendCode','')
            return "sucess"
    return "error"

##############################################################################
# Online Chatting System
##############################################################################

# create room
@app.route('/createroom', methods=['GET','POST'])
def createroom():
    resp = {'status': 'success'}
    data = get_room_info()
    roomid = data['roomid']
    if not have_chatroom(roomid):
        create_chatroom(roomid)
        resp['message'] = 'N'
    else:
        # history = get_comment(roomid)
        resp['message'] = 'Y'
        # resp['chathistory'] = history
    return jsonify(resp)

# join room
@app.route('/joinroom',methods=['GET','POST'])
def joinroom():
    resp = {'status': 'success'}
    data = get_room_info()
    roomid = data['roomid']
    # print(have_chatroom(roomid))
    if not have_chatroom(roomid):
        resp['message'] = 'N'
    else:
        history = get_comment(roomid)
        # print(history)
        resp['message'] = 'Y'
        resp['chathistory'] = history
    return jsonify(resp)

# load chat history
@app.route('/chat', methods=['GET','POST'])
def add_history():
    resp = {'status': 'success'}
    data = get_chat_info()
    if add_comment(data):
        return jsonify(resp)
    else:
        return jsonify({'status': 'error'})

# socket
@socketio.on('joinRoom')
def on_join(data):
    room = data['roomID']
    join_room(room)

# socket broadcast
@socketio.on('msg')
def on_msg(data):
    pkg = {'username':data['email'],'contents':data['msg'],'roomid':data['roomID']}
    add_comment(pkg)                            # 将信息同时加入数据库
    emit('broadcastMsg', data, broadcast=True)

# 在线编译代码
@app.route('/compilejs', methods=['GET','POST'])
def compilejs():
    response_object = {'status': 'success'}
    post_data = request.get_json()
    js = post_data.get('sendCode')
    js = js.replace('\n', '').replace('\r', '').replace('\t','')
    try:
        ctx = execjs.compile(js)
        response_object['answer'] = ctx.call("main")
    except:
        response_object['message'] = 'N'
        return jsonify(response_object)
    response_object['message'] = 'Y'
    return jsonify(response_object)


if __name__=='__main__':
    socketio.run(app, port=5000,debug=True, host='0.0.0.0')
    