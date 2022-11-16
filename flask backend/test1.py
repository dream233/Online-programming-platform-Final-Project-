import pymongo

conn_str = "mongodb+srv://charles:charles123456@cluster0.8nx4ghy.mongodb.net/test"
client = pymongo.MongoClient(conn_str, serverSelectionTimeoutMS=5000)
db = client["cse503final"]
users = db["users"]

results = users.find({"email":email}) # 没有查询到会返回一个cursor，results.count()方法已经废弃
results = users.find_one({"email":email}) # 没有查询到会返回None，用 if results != None: 处理

results = users.count_documents({"email":"email"}) # 没有查询到会返回0，用这个进行预查询
print(results)
