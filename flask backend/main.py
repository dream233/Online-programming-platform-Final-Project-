from database import match_user
from flask import Flask, jsonify
from flask_cors import CORS

from database import *
from interface import *

app = Flask(__name__)
app.config.from_object(__name__)

# enable CORS
CORS(app, supports_credentials=True)

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
    if not have_user(email):        # 判断用户名称是否已经存在
        if create_user(uinfo):      # 创建用户
            resp['message'] = 'Y'
        else:
            resp['message'] = 'N'
            resp['error'] = "服务器错误"
    else:
        resp['message'] = 'N'
        resp['error'] = '用户已经存在'
    return jsonify(resp)

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

@app.route('/addproblem',methods=['POST','GET'])
def add_problem():
    pass

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
    if alter_problem(prob_info['id'],prob_info):
        resp['message'] = 'Y'
    else:
        resp['message'] = 'N'
    return jsonify(resp)
    
# 创建聊天房间
@app.route('/createroom', methods=['GET','POST'])
def create_room():
    pass

# 获取聊天记录
@app.route('/history', methods=['GET','POST'])
def get_chat_history():
    pass

# 发送接收面试题
li = [1]

@app.route('/getcode', methods=['GET'])
def get_code():
    return li[0]

@app.route('/postcode', methods=['POST'])
def post_code():
    data = request.get_json()
    if data['sendRoom'] == '200':
        li[0] = data['sendCode']
        return "message get"
    else:
        return "wrong roomNum"

if __name__=='__main__':
    app.run(host='0.0.0.0',port=5000,debug=True)