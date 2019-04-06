from db import user_collection

def signup_db(firstname,lastname,email,username,password,address):
    new_post = {
        "First Name": firstname,
        "Last Name": lastname,
        "Email": email,
        "Username": username,
        "Password": password,
        "Address": address,
        }
    user_collection.insert_one(new_post)