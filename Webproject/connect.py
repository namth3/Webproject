from db import user_collection

def signup_db(firstname,lastname,email,username,password):
    new_post = {
        "First Name": firstname,
        "Last Name": lastname,
        "Email": email,
        "Username": username,
        "Password": password,
        }
    user_collection.insert_one(new_post)