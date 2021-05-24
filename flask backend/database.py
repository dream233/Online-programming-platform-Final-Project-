import pyodbc
from uuid import uuid1

db = pyodbc.connect("DRIVER={SQL Server};SERVER=111.229.68.117,1433;DATABASE=online_programming_platform;UID=pyserver;PWD=1ybaHlY5xJ")
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
    problem:题目信息{owner,password,contents}
    return:bool
    """
    problem_id = uuid1().hex
    try:
        cur.execute("insert into problems(problem_id,owner_id,password,contents) values(?,?,?,?)",[problem_id,problem['owner'],problem['password'],problem['contents']])
        db.commit()
    except:
        cur.rollback()
        return False
    return True

def get_problem(problem_id:str,password:str)->dict:
    """获取题目信息
    problem_id:题目编号
    password:题目密码
    return:题目信息{id,owner,contents}
    """
    try:
        cur.execute("select * from problems where problem_id=?",problem_id)
        row = cur.fetchone()
        if not row:
            return None
        elif password == row[2]:
            res = {'id':row[0],'owner':row[1],'contents':row[3]}
            return res
        else: 
            return {'id':0}
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
        cmt = [comment['room_id'],comment['username'],comment['contents']]
        cur.execute("insert into comments(room_id,username,comment_time,contents) values (?,?,getdate(),?)",cmt)
        db.commit()
    except:
        cur.rollback()
        return False
    return True

def get_comment(interviewer:str,interviewee:str)->list:
    """获取留言
    interviewer:面试官
    interviewee:面试者
    return:留言信息列表[{interviewer,interviewee,time,content}]
    """
    res = []
    tmp = [interviewer,interviewee,interviewee,interviewer]
    cur.execute("select * from comments where (interviewer=? and interviewee=?) or (interviewer=? and interviewee=?) order by comment_time desc",tmp)
    tmp = cur.fetchall()
    for row in tmp:
        res.append(dict(zip(['interviewer','interviewee','time','content'],row)))
    return res


info = {'interviewer':'123','interviewee':'12553','contents':'hello world'}
prob = {'owner':'123','password':'233','contents':'fiafgoahifiuagkuhae==='}
uinfo = {'email':'123','username':'1245','password':'159','type':'1'}
uinfo2 = {'email':'12553','username':'1245','password':'159','type':'1'}
# create_problem(prob)
# add_comment(info)
# create_user(uinfo)
# create_user(uinfo2)


# print( match_user('1234','159') )

