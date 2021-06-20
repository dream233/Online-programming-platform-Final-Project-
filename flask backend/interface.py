from flask import request

def get_login_info():
    """获取登陆信息
    return:登陆信息{email,password,usertype}
    """
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
    """获取注册信息
    return:注册信息{email,username,password,usertype}
    """
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

def get_code_info():
    """获取代码信息
    return:代码信息{type,sendRoom,sendCode}
    """
    data = request.get_json()
    try:
        tp = data['type']
    except:
        data['type'] = 0
    return data

def get_room_info():
    """获取房间信息
    return:房间信息{roomid}
    """
    data = request.get_json()
    res = {}
    try:
        res['roomid'] = data['roomID']
    except:
        return None
    return res

def get_chat_info():
    """获取聊天信息
    return:聊天信息{roomid，username,contents}
    """
    data = request.get_json()
    res = {}
    try:
        res['roomid'] = data['roomID']
        res['username'] = data['email']
        res['contents'] = data['msg']
    except:
        return None
    return data
