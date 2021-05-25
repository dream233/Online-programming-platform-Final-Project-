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
        # res['email'] = data.get['email']
        res['email'] = data.get('name')
    except:
        return None
    return res

def get_reg_info():
    data = request.get_json()
    res = {}
    try:
        res['username'] = data.get('name')
        res['password'] = data.get('password')
        if data.get('id') == 'interviewer':
            res['usertype'] = '2'
        else:
            res['usertype'] = '1'
        # res['email'] = data.get['email']
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