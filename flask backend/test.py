# document
# https://www.mongodb.com/docs/manual/reference/operator/update/
# https://www.youtube.com/watch?v=rE_bJl2GAY8

import pymongo

# Replace the uri string with your MongoDB deployment's connection string.
# conn_str = "mongodb+srv://andrew:andrew123456@cluster0.xt8z1tf.mongodb.net/test"
conn_str = "mongodb+srv://charles:charles123456@cluster0.8nx4ghy.mongodb.net/test"

# set a 5-second connection timeout
# which cluster to use
client = pymongo.MongoClient(conn_str, serverSelectionTimeoutMS=5000)

# which db to use
db = client["cse503final"]

# which collection to use
collection = db["users"]

# # try:
# #     print(client.server_info())
# # except Exception:
# #     print("Unable to connect to the server.")

# # insert one
# post  = {"name":"charles", "password":"123456"}
# collection.insert_one(post)

# # insert many
# post1  = {"name":"charles", "password":"123456"}
# post2  = {"name":"andrew", "password":"123456"}
# collection.insert_many([post1,post2])

# # find
# results = collection.find({"name":"charles"})

# # find with many constraints
# results = collection.find({"name":"charles","password":"123456"})

# # find the first one
# results = collection.find_one({"name":"charles"})

# # find everything
# results = collection.find({})

# # for result in results:
# #     print(result)

# # delete (same to find)
# results = collection.delete({"name":"charles"})

# # update one / many
# results = collection.update_one({"name":"charles"}, {"$set":{"name":"charles1"}}) # change value
# results = collection.update_one({"name":"charles"}, {"$set":{"hello":"hi"}}) # add value

# # how many posts/documents in collection 
# post_count = collection.count_documents({})
# print(post_count)


results = collection.find_one({"name":"charles22"})
print(results)