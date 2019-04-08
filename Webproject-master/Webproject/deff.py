from db import post_collection,user, user_post
from bson import ObjectId
import random
homepage_post_list=post_collection.find().sort([("_id", -1), ("date", -1)])
user_post_li=user_post.find().sort([("_id", -1), ("date", -1)])
post_list = []
for i in user_post_li:
    post_list.append(i)
  


# def add(title,link1,link2,link3,link4,link5,link6,content):
#     new={
#         "Title":title,
#         "img_link":[link1,link2,link3,link4,link5,link6],
#         "content":content,
#     }
#     post_collection.insert_one(new)
# if __name__=="__main__":
#     add("mot con rua","https://taianhdep.vn/wp-content/uploads/2018/01/tai-hinh-nen-thien-nhien-4k-dep-44.jpg",
#     "http://nvhb.net/wp-content/uploads/2018/09/Autumn-23.jpg",
#     "https://www.sony.com.ph/image/bc6d25fa6371c2899ce704a2bed7614c?fmt=png-alpha&wid=960",
#     "https://avatars.mds.yandex.net/get-pdb/225396/104d1bfc-b497-443a-b488-1ca4711de18f/s1200",
#     "http://yodobi.com/4k-Wallpapers/4k-wallpapers-mobile-Is-4K-Wallpaper.jpg",
#     "https://i.imgur.com/EdAGGFS.jpg",
#     " day la noi dung day la noi dung day la noi dung day la noi dung day la noi dung day la noi dung day la noi dung day la noi dung day la noi dung day la noi dung day la noi dung day la noi dung day la noi dung day la noi dung day la noi dung day la noi dung day la noi dung day la noi dung day la noi dung day la noi dung day la noi dung day la noi dung day la noi dung day la noi dung day la noi dung day la noi dung day la noi dung day la noi dung day la noi dung day la noi dung day la noi dung day la noi dung day la noi dung day la noi dung day la noi dung day la noi dung day la noi dung day la noi dung day la noi dung day la noi dung day la noi dung day la noi dung day la noi dung day la noi dung day la noi dung day la noi dung day la noi dung day la noi dung")

# list_id=[]
# for i in homepage_post_list:
#     list_id.append(i["_id"])
# def get_by_id(id):
#     post = post_collection.find_one({'_id': ObjectId(id)})
#     return post

# def post_list():
#     post_list = post_collection.find({})
#     return post_list


# use = []
# for i in user_post_list:
#     use.append(i)
# print(use)


# lenn=len(posttt)-1
# post_list_1=[]
# post_list=[]
# #print(lenn)
# for i in range(0,lenn,2):
#     post_list_1 = []
#     post_list_1.append(posttt[i])
#     post_list_1.append(posttt[i+1])
#     post_list.append(post_list_1)

    
# print(post_list[0][0]["Title"])



# def delete_by_id(id):
#     user_post.delete_one({'_id': ObjectId(id)})

# for i in range(14):
#     delete_by_id(nar[i])

# ss=get_by_id(a[0])
# print (ss["img_link"][3])
# if __name__=="__main__":
#     print(a)
# def add_new(name,price):
#     new_food={
#         "name":name,
#         "price":price,
#     }
#     food_collection.insert_one(new_food)

# def get(query):
#     food_list = food_collection.find(query)
#     return food_list





# def update_by_id(id,name,price):
#     query={'_id': ObjectId(id)}
#     update = { "$set":{"name":name},
#             "$set":{"price":price},
#      }
#     food_collection.find_one_and_update(query,update)

# def add(username,password):
#     new={
#         "USERNAME":username,
#         "PASSWORD":password,
#     }
#     user_collection.insert_one(new)


# def find_by_username(username):
#     info = user_collection.find_one({"USERNAME":username})
#     return info

