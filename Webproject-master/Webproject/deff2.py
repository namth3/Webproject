from db import post_collection,user,user_post
from bson import ObjectId
import random
listt=user_post.find().sort([("_id", -1), ("date", -1)])


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

nar=[]
for i in listt:
    nar.append(i["_id"])
    print(i)
def get_by_id(id):
    f=post_collection.find_one({'_id': ObjectId(id)})
    return f


# a=get_by_id(nar[0])
# # a1=a["Title"]
# # a2=a["img_link"]
# # content1=a["content"]
# print(a)




# b=get_by_id(nar[1])
# b1=b["Title"]
# b2=b["img_link"]
# content2=b["content"]

# c=get_by_id(nar[2])
# c1=c["Title"]
# c2=c["img_link"]
# content3=c["content"]

# d=get_by_id(nar[3])
# d1=d["Title"]
# d2=d["img_link"]
# content4=d["content"]

# e=get_by_id(nar[3])
# e1=e["Title"]
# e2=e["img_link"]
# content5=e["content"]

# f=get_by_id(nar[3])
# f1=f["Title"]
# f2=f["img_link"]
# content6=f["content"]

# g=get_by_id(nar[3])
# g1=g["Title"]
# g2=g["img_link"]
# content7=g["content"]

# h=get_by_id(nar[3])
# h1=h["Title"]
# h2=h["img_link"]
# content8=h["content"]


# print(e2)
# # def delete_by_id(id):
#     post_collection.delete_one({'_id': ObjectId(id)})

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

