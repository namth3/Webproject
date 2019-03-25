



from pymongo import MongoClient
uri = "mongodb+srv://c4e_travel:travel1@place-k07pp.mongodb.net/test?retryWrites=true"
    # Connect
client = MongoClient(uri)

    # Get database
def db_connect_Vung (TenVung):
    db = client.TenVung
    return db

    #3.Get collection
def db_connect_DiaDiem(db,DiaDiem):
    post_collection = db[DiaDiem]
    return post_collection #collection



#6. Close connection
def close():
    client.close()