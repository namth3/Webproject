from db import post_collection

def add_post(title,img,p):

    new_post = {
        "Title" :title,
        "img_link": img,
        "content" : p,
    }
    post_collection.insert_one(new_post)

# def add_user(name,password):
#     new_user = {
#         "username" :name,
#         "password": password,
#     }
#     user_collection.insert_one(new_user)



# def get(query):
#     food_list= food_collection.find(query)
#     return food_list

# def get_by_id(id):
#     f = food_collection.find_one({ "_id": ObjectId(id)})
#     return f

# def delete_by_id(id):
#     f =  food_collection.delete_one({"_id": ObjectId(id)})

# def update_by_id(id,updater,nd,up,dp):
#     query = {"_id": ObjectId(id)}
#     updater = {dp: {nd: up}}#inc,$dec,$set,$unset
#     food_collection.find_one_and_update(query,updater)

# def find_by_username(username):
#     f = user_collection.find_one({"username": username})
#     return f

# if __name__=="__main__":
#     print(find_by_username('admin'))
