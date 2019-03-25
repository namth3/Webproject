from pymongo import MongoClient

uri = "mongodb+srv://c4e_travel:travel1@place-k07pp.mongodb.net/test?retryWrites=true"
# Connect
client = MongoClient(uri)

# Get database
db = client.User

#3.Get collection
user = db["users"] #collection



#6. Close connection
def close():
    client.close()