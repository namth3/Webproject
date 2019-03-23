from pymongo import MongoClient
url = "mongodb+srv://namth3:MN1Cbt6BFOvUIExD@cluster0-kondi.mongodb.net/test?retryWrites=true"

#1.connect
client = MongoClient(url)


#2. Get DB
db = client.test

#3. get collection
food_collection = db["food"]
user = db["user"]