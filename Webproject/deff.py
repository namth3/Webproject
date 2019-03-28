from db import post_collection,user
from bson import ObjectId
import random
listt=post_collection.find()
nar=[]
no=[]

for i in listt:
    nar.append(i["Title"])
a=(random.choices(nar))
no.append(a)
while(True):
    b=(random.choices(nar))
    if b not in no:
        break
no.append(b)

while(True):
    c=(random.choices(nar))
    if c not in no:
        break
no.append(c)

while(True):
    d=(random.choices(nar))
    if d not in no:
        break
no.append(d)

while(True):
    e=(random.choices(nar))
    if e not in no:
        break
no.append(e)



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

# def get_by_id(id):
#     f=food_collection.find_one({'_id': ObjectId(id)})
#     return f

# def delete_by_id(id):
#     food_collection.delete_one({'_id': ObjectId(id)})

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

