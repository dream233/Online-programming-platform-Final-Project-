from flask import Flask, jsonify, request
from flask_cors import CORS



Users = [
    {
        'name': '123',
        'password': '123',
        'id': 'candidate'
    },
{
        'name': '123',
        'password': '123',
        'id': 'interviewer'
    }
]

# configuration
DEBUG = True

# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})


# sanity check route

def sql_regsiter(data):
    for user in Users:
        if(data.get('name')==user.get('name') and data.get('id')==user.get('id')):
            return False
    return True
@app.route('/register', methods=['GET','POST'])
def register():
    response_object = {'status': 'success'}
    data = request.get_json()
    response_object['user'] = data
    if sql_regsiter(data):
        if data.get('id')=='1':
            data['id'] = 'candidate'
        else:
            data['id'] = 'interviewer'
        Users.append(data)
        response_object['message'] = 'Y'
    else:
        response_object['message'] = 'N'
    return jsonify(response_object)


def sql_login(data):
    for user in Users:
        if (data.get('name')==user.get('name') and data.get('password')==user.get('password') and data.get('id')==user.get('id')):
            return True
    return False
@app.route('/login', methods=['GET', 'POST'])
def login():
    response_object = {'status': 'success'}
    post_data = request.get_json()
    print(post_data)
    if sql_login(post_data):
        response_object['message'] = 'Y'
    else:
        response_object['message'] = 'N'
    return jsonify(response_object)


if __name__ == '__main__':
    app.run(host="192.168.1.200",port=5000)