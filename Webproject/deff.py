from db import post_collection,user
from bson import ObjectId
import random
listt=post_collection.find()
nar=[]
no=[]

for i in listt:
    nar.append(i["_id"])
a=(random.choices(nar))
no.append(a[0])
while(True):
    b=(random.choices(nar))
    if b not in no:
        break
no.append(b[0])

while(True):
    c=(random.choices(nar))
    if c not in no:
        break
no.append(c[0])

while(True):
    d=(random.choices(nar))
    if d not in no:
        break
no.append(d[0])

while(True):
    e=(random.choices(nar))
    if e not in no:
        break
no.append(e[0])

def get_by_id(id):
    f=post_collection.find_one({'_id': ObjectId(id)})
    return f


a=get_by_id(no[0])
a1=a["Title"]
a2=a["img_link"]


b=get_by_id(no[2])
b1=b["Title"]
b2=b["img_link"]

c=get_by_id(no[3])
c1=c["Title"]
c2=c["img_link"]

d=get_by_id(no[0])
d1=d["Title"]
d2=d["img_link"]

e=get_by_id(no[4])
e1=e["Title"]
e2=e["img_link"]

# def delete_by_id(id):
#     post_collection.delete_one({'_id': ObjectId(id)})
#delete_by_id(nar[0])

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

