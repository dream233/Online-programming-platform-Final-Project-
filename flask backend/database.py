import pyodbc

# db = pyodbc.connect("DRIVER={ODBC Driver 17 for SQL Server};SERVER=111.229.68.117,1433;DATABASE=online_programming_platform;UID=pyserver;PWD=1ybaHlY5xJ")
db = pyodbc.connect("DRIVER={ODBC Driver 17 for SQL Server};SERVER=localhost;DATABASE=online_programming_platform;UID=pyserver;PWD=pyserver")
cur = db.cursor()

def create_user(userinfo:dict):
    """创建用户
    userinfo:{username,email,password,usertype}
    return:bool
    """
    try:
        cur.execute("insert into users(username,email,password,usertype) values(?,?,?,?)",[userinfo['username'],userinfo['email'],userinfo['password'],userinfo['usertype']])
        db.commit()
    except:
        cur.rollback()
        return False
    return True

def have_user(email:str)->bool:
    """查询是否存在此用户
    email:邮箱地址
    return:bool
    """
    try:
        cur.execute("select * from users where users.email=?",email)
        if cur.fetchone():
            return True
    except:
        cur.rollback()
    return False

def match_user(email:str,password:str,usertype:str)->dict:
    """查询邮箱密码是否匹配
    email:邮箱地址
    password:密码
    usertype:用户种类
    return:用户信息{email,username,type}
    """
    try:
        cur.execute("select * from users where users.email=?",email)
        row = cur.fetchone()
        if not row:
            return None
        if row[2] == password and row[3] == usertype:
            info = {'email':row[0],'username':row[1],'type':row[3]}
            return info
    except:
        cur.rollback()
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

def alter_problem(problem_id:str,new_problem:dict)->str:
    """修改问题
    problem_id:问题编号
    new_problem:新问题信息{owner,password,contents}
    return:bool
    """
    try:
        info = [new_problem['owner'],new_problem['password'],new_problem['contents'],problem_id]
        cur.execute("update problems set owner=?,password=?,contents=? where problem_id=?",info)
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
        cur.execute("insert into chatroom(room_id) values(?)",roomid)
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
        cur.execute("select * from chatroom where room_id=?",roomid)
        if cur.fetchone():
            return True
    except:
        cur.rollback()
    return False

def get_comment(roomid:str)->list:
    """获取留言
    roomid:房间号
    return:留言信息列表[{'roomid','username','email','time','contents'}]
    """
    try:
        res = []
        cur.execute("select room_id,users.username,email,comment_time,contents from comments,users where comments.room_id=? and comments.username=users.email order by comment_time asc",roomid)
        for row in cur.fetchall():
            tmp = {'roomID':row[0],'username':row[1],'email':row[2],'time':row[3][:-8],'msg':row[4]}
            res.append(tmp)
        return res
    except:
        cur.rollback()
    return None
"""
info = {'roomid':'123','username':'12553','contents':'hello world'}
prob = {'owner':'123','password':'233','contents':'fiafgoahifiuagkuhae==='}
uinfo = {'email':'123','username':'1245','password':'159','type':'1'}
uinfo2 = {'email':'12553','username':'1245','password':'159','type':'1'}
# create_problem(prob)
# add_comment(info)
# create_user(uinfo)
# create_user(uinfo2)
tp = create_chatroom("13")

print( list_problemid() )
"""
