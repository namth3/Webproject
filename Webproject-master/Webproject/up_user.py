from db import post_collection, user_post

def add_user_post(title,username,img,p,location,vehicle,tipsfortravel):

    new_post = {
        "Title" :title,
        "Username": username,
        "img_link": img,
        "content" : p,
        "location": location,
        "vehicle": vehicle,
        "tipsfortravel": tipsfortravel,
    }
    user_post.insert_one(new_post)