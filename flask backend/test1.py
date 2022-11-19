import pymongo

conn_str = "mongodb+srv://charles:charles123456@cluster0.8nx4ghy.mongodb.net/test"
client = pymongo.MongoClient(conn_str, serverSelectionTimeoutMS=5000)
db = client["cse503final"]
users = db["users"]
problems = db["problems"]
comments = db["comments"]
chatrooms = db["chatrooms"]

roomid = "00000001"

# results = users.find_one({"email":email}) # 没有查询到会返回一个cursor，results.count()方法已经废弃
# results = users.find_one({"email":email}) # 没有查询到会返回None，用 if results != None: 处理

# results = users.count_documents({"email":"email"}) # 没有查询到会返回0，用这个进行预查询
# print(results)


pipeline = [
    {
        "$lookup":{
            "from": "users",       # other table name
            "localField": "username",   # name of users table field
            "foreignField": "email", # name of userinfo table field
            "as": "user_info"         # alias for userinfo table
        }
    },
    {   "$unwind":"$user_info" },     # $unwind used for getting data in object or for one record only

    # // define some conditions here 
    {
        "$match":{
            "$and":[{"room_id" : roomid}]
        }
    }

    # # // define which fields are you want to fetch
    # {   
    #     "$project":{
    #         "room_id" : 1,
    #         "email" : "$users.email",
    #         # "comment_time" : 1,
    #         "username" : "$users.username",
    #         "contents" : 1,
    #         # "usertype" : 1
    #     } 
    # }
]

results = db.comments.aggregate(pipeline)

for result in results:
        usertype = result["user_info"]["usertype"]
        if usertype == '2':
            usertype = 'interviewer'
        else:
            usertype = 'candidate'
        # tmp = {'roomID':result["room_id"],'username':result["username"],'email':result["email"],'time':result[3].strftime('%Y-%m-%d %H:%M:%S'),'msg':result[4],'type':usertype}
        
        tmp = {'roomID':result["room_id"],'username':result["username"],'email':result["user_info"]["email"],'msg':result["contents"], 'type':usertype}
        print(tmp)