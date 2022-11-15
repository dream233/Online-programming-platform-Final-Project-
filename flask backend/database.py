import pymongo

conn_str = "mongodb+srv://charles:charles123456@cluster0.8nx4ghy.mongodb.net/test"
client = pymongo.MongoClient(conn_str, serverSelectionTimeoutMS=5000)
db = client["cse503final"]
users = db["users"]

def create_user(userinfo:dict):
    """创建用户
    userinfo:{username,email,password,usertype}
    return:bool
    """
    try:
        # cur.execute("insert into users(username,email,password,usertype) values(?,?,?,?)",[userinfo['username'],userinfo['email'],userinfo['password'],userinfo['usertype']])
        # db.commit()
        post  = {"username":userinfo['username'], "email":userinfo['email'], "password":userinfo['password'],"usertype":userinfo['usertype']}
        users.insert_one(post)
    except:
        # cur.rollback()
        return False
    return True

def have_user(email:str)->bool:
    """查询是否存在此用户
    email:邮箱地址
    return:bool
    """
    try:
        # cur.execute("select * from users where users.email=?",email)
        results = users.find({"email":email})
        if results != "None":
            return True
    except:
        # cur.rollback()
        print("error")
    return False

def get_user_info(email:str)->dict:
    """查询用户信息
    email:邮箱地址
    return:用户信息{email,username,password,type}
    """
    try:
        # cur.execute("select * from users where users.email=?",email)
        # row = cur.fetchone()
        # if not row:
        #     return None
        
        # info = {'email':row[0],'username':row[1],'password':row[2],'type':row[3]}
        results = users.find({"email":email})
        if results == "None":
            return True

        info = {'email':results[0],'username':results[1],'password':results[2],'type':results[3]}
        return info
    except:
        # cur.rollback()
        print("error")
    return None

def create_problem(problem:dict):
    """创建题目
    problem:题目信息{id,owner,password,contents}
    return:bool
    """
    try:
        cur.execute("insert into problems(problem_id,owner_id,password,contents) values(?,?,?,?)",[problem['id'],problem['owner'],problem['password'],problem['contents']])
        db.commit()
    except:
        cur.rollback()
        return False
    return True

def get_problem(problem_id:str)->dict:
    """获取题目信息
    problem_id:题目编号
    return:题目信息{id,password,owner,contents}
    """
    try:
        cur.execute("select * from problems where problem_id=?",problem_id)
        row = cur.fetchone()
        return dict(zip(['id','owner','password','contents'],row))
    except:
        cur.rollback()
        return None

def list_problemid()->list:
    """显示题目列表
    return:题目ID列表[{id}]
    """
    try:
        res = []
        cur.execute("select problem_id from problems")
        for row in cur.fetchall():
            res.append({'id':row[0]})
        return res
    except:
        cur.rollback()
    return None

def alter_problem(problem_id:str,new_problem:dict)->bool:
    """修改问题
    problem_id:问题编号
    new_problem:新问题信息{owner,password,contents}
    return:bool
    """
    try:
        info = [new_problem['contents'],problem_id]
        cur.execute("update problems set contents=? where problem_id=?",info)
        db.commit()
    except:
        cur.rollback()
        return False
    return True

def delete_problem(problem_id:str)->bool:
    """删除题目
    problem_id:题目编号
    return:bool
    """
    try:
        cur.execute("delete from problems where problem_id=?",problem_id)
        db.commit()
    except:
        cur.rollback()
        return False
    return True

def add_comment(comment:dict)->bool:
    """增加留言
    comment:留言信息{room_id,username,contents}
    return:bool
    """
    try:
        cmt = [comment['roomid'],comment['username'],comment['contents']]
        cur.execute("insert into comments(room_id,username,comment_time,contents) values (?,?,getdate(),?)",cmt)
        db.commit()
    except:
        cur.rollback()
        return False
    return True

def create_chatroom(roomid:str)->bool:
    """创建聊天室
    roomid:房间号
    return:bool
    """
    try:
        cur.execute("insert into chatrooms(room_id) values(?)",roomid)
        db.commit()
    except:
        cur.rollback()
        return False
    return True

def have_chatroom(roomid:str)->bool:
    """判断是否存在聊天室
    roomid:房间号
    return:bool
    """
    try:
        cur.execute("select * from chatrooms where room_id=?",roomid)
        if cur.fetchone():
            return True
    except:
        cur.rollback()
    return False

def get_comment(roomid:str)->list:
    """获取留言
    roomid:房间号
    return:留言信息列表[{'roomid','username','email','time','contents','usertype}]
    """
    try:
        res = []
        cur.execute("select room_id,users.username,email,comment_time,contents,usertype from comments,users where comments.room_id=? and comments.username=users.email order by comment_time asc",roomid)
        for row in cur.fetchall():
            usertype = row[5]
            if usertype == '2':
                usertype = 'interviewer'
            else:
                usertype = 'candidate'
            tmp = {'roomID':row[0],'username':row[1],'email':row[2],'time':row[3].strftime('%Y-%m-%d %H:%M:%S'),'msg':row[4],'type':usertype}
            res.append(tmp)
        return res
    except:
        cur.rollback()
    return None
