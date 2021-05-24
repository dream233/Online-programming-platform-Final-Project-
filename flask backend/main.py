from werkzeug.wrappers import response
from database import match_user
from logging import error
from flask import Flask, render_template, request, jsonify
from flask.globals import session
from flask.helpers import url_for
from werkzeug.utils import redirect
from functools import wraps
from flask_cors import CORS

from database import *
from interface import *

app = Flask(__name__)
app.config.from_object(__name__)

# enable CORS
CORS(app, supports_credentials=True)

"""
# 包装器，包装登陆才能访问的内容
def login_required(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if session.get('username'):
            return func(*args, **kwargs)
        else:
            return redirect(url_for('login', next=request.url))
    return wrapper
"""
# 注册
@app.route('/register',methods=['POST','GET'])
def register():
    uinfo = get_reg_info()        # 获取登陆信息
    resp = {'status': 'success'}
    if not uinfo:                   # 如果用户信息不全面，直接报错
        resp['status'] = 'error'
        resp['message'] = 'N'
        return jsonify(resp)
    
    email = uinfo['email']
    if not have_user(email):        # 判断用户名称是否已经存在
        if create_user(uinfo):      # 创建用户
            resp['message'] = 'Y'
        else:
            resp['message'] = 'N'
    else:
        resp['message'] = 'N'
    return jsonify(resp)

# 登陆    
@app.route('/login',methods=['POST','GET'])
def login():
    uinfo = get_login_info()
    resp = {'status': 'success'}
    if not uinfo:                   # 如果用户信息不全面则返回错误
        resp['status'] = 'error'
        resp['message'] = 'N'
        return jsonify(resp)
    
    # 能否查询到这个用户的信息
    user_info = match_user(uinfo['email'],uinfo['password'],uinfo['usertype'])
    if not user_info:
        resp['message'] = 'N'
        resp['username'] = ""
    else:
        resp['message'] = 'Y'
        resp['username'] = user_info['username']        # 登陆成功还返回用户名称
    
    return jsonify(resp)

"""
# 登出
@app.route('/logout/')
@login_required
def logout():
    session.pop('username', None)
    session.pop('usertype', None)
    session.pop('email', None)
    redirect(url_for('/login'))

# 主页
@app.route('/index/')
@login_required
def index():
    return render_template('index.html')
"""
"""
# 访问试题
@app.route('/problems',methods=['POST','GET'])
def return_problem():
    pinfo = get_dict()
    problem = get_problem(pinfo['id'],pinfo['password'])
    if not problem:
        send_msg('404')
    elif problem['id'] == 0:
        send_msg('wrong')
    else:
        send_msg('sucess')
        send_dict(problem)
        
    return render_template('problem.html')

# 添加试题
@app.route('/problems/add',methods=['GET','POST'])
def addproblem():
    problem = get_dict()
    if session['usertype'] != 'interviewer':    # 用户类型不是面试官不允许创建试题
        send_msg('no permission')

    problem['owner'] = session['email'] 
    try:
        create_problem(problem)
    except:
        error('unknown error of server')
"""
if __name__=='__main__':
    app.run(debug=True)