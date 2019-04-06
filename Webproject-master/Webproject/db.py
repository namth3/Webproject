from pymongo import MongoClient

uri = "mongodb+srv://c4e_travel:travel1@place-k07pp.mongodb.net/test?retryWrites=true"
# Connect
client = MongoClient(uri)

# Get database
db = client.travel
db_user = client.User
check = client.check

#3.Get collection
user_collection = db_user["users"] #collection

#3.Get collection
 #collection
post_collection = db["BaiVietTongHop"]
user = db["user"]
user_post=db["user_post"]

# for i in post_collection.find():
#     print (i["Title"])
# listt=post_collection.find()
# for i in listt:
#     print (i["Title"])

#4. create new document



#6. Close connection
def close():
    client.close()