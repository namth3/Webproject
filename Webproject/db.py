from pymongo import MongoClient

uri = "mongodb+srv://c4e_travel:travel1@place-k07pp.mongodb.net/test?retryWrites=true"
# Connect
client = MongoClient(uri)

# Get database
db = client.travel
db_user = client.User

#3.Get collection
user_collection = db_user["users"] #collection

#3.Get collection
post_collection = db["BaiVietTongHop"] #collection
user = db["user"]

# listt=post_collection.find()
# for i in listt:
#     print (i["Title"])

#4. create new document
new_user = {
    "username" :"daihiep1707",
    "password": "thanhninh"
}


#6. Close connection
def close():
    client.close()