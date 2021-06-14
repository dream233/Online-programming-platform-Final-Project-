from flask import request

def get_login_info():
    data = request.get_json()
    res = {}
    try:
        res['password'] = data.get('password')
        if data.get('id') == 'interviewer':
            res['usertype'] = '2'
        else:
            res['usertype'] = '1'
        res['email'] = data.get('name')
    except:
        return None
    return res

def get_reg_info():
    data = request.get_json()
    res = {}
    try:
        res['username'] = data.get('username')
        res['password'] = data.get('password')
        if data.get('id') == 'interviewer':
            res['usertype'] = '2'
        else:
            res['usertype'] = '1'
        res['email'] = data.get('name')
    except:
        return None
    return res
    
def get_req_of_problem():
    data = request.get_json()
    res = {}
    try:
        res['id'] = data.get('id')
    except:
        return None
    return res

def get_problem_info():
    data = request.get_json()
    return data

def get_code_info():
    data = request.get_json()
    try:
        tp = data['type']
    except:
        data['type'] = 0
    return data

def get_room_info():
    data = request.get_json()
    res = {}
    try:
        res['roomid'] = data['roomID']
    except:
        return None
    return res

def get_chat_info():
    data = request.get_json()
    res = {}
    try:
        res['roomid'] = data['roomID']
        res['username'] = data['email']
        res['contents'] = data['msg']
    except:
        return None
    return data
