import os
from flask import Flask, flash, request, redirect, url_for, render_template, session
from db import *
from bson import ObjectId
from connect import signup_db
#from db import post_collection,user
from deff import *
app = Flask(__name__)

app.config["SECRET_KEY"] = "@thanhinh1707abcdefghiklmn"

def find_username(username):
    user_list = user_collection.find_one({"Username":username})
    return user_list

@app.route("/")
def home_page():
# <<<<<<< HEAD
    
#      return render_template("index.html")



# =======
#     locations = ["Đà Lạt","Thành Phố Hồ Chí Minh","Đà Nẵng", "Hà Nội", "Thị Trấn Sapa"]
#     return render_template("index.html", locati = locations,a1=a1,b1=b1,c1=c1,d1=d1,e1=e1,f1=f1,g1=g1,h1=h1,a2=a2,b2=b2,c2=c2,d2=d2,e2=e2,f2=f2,g2=g2,h2=h2)

# @app.route("/image1")
# def image1():
#     return render_template("image1.html",a2=a2,b2=b2,c2=c2,d2=d2,e2=e2,content1=content1)
# @app.route("/image2")
# def image2():
#     return render_template("image2.html",a2=a2,b2=b2,c2=c2,d2=d2,e2=e2,content2=content2)
# @app.route("/image3")
# def image3():
#     return render_template("image3.html",a2=a2,b2=b2,c2=c2,d2=d2,e2=e2,content3=content3)
# @app.route("/image4")
# def image4():
#     return render_template("image4.html",a2=a2,b2=b2,c2=c2,d2=d2,e2=e2,content4=content4)
# @app.route("/image5")
# def image5():
#     return render_template("image5.html",a2=a2,b2=b2,c2=c2,d2=d2,e2=e2,content5=content5)
# @app.route("/image6")
# def image6():
#     return render_template("image6.html",f2=f2,content6=content6)
# @app.route("/image7")
# def image7():
#     return render_template("image7.html",g2=g2,content7=content7)
# @app.route("/image8")
# def image8():
#     return render_template("image8.html",h2=h2,content8=content8)
# >>>>>>> f5fa5a29c3513251b86d4849367add7aca23e28e
    return "Hello"

@app.route("/login",  methods=["GET","POST"])
def login():
    if request.method == "GET":
        return render_template("login.html")
    elif request.method == "POST":
        form = request.form
        u = form["username"]
        p = form["password"]
        u_list = find_username(u)
        if u_list == None:
            return "No such user"
        elif u_list["Password"] != p:
            return "Wrong password"
        else:
            # id_user = u_list["_id"]
            session["token"] = u
            # a = session["token"]
            return  "Dang nhap thanh cong"
        return redirect('/')





@app.route("/signup",  methods=["GET","POST"])
def signup():
    if request.method == "GET":
        return render_template("signup.html")
    elif request.method == "POST":
        form = request.form
        sign_name = form["First Name"]
        sign_l_name = form["Last Name"]
        sign_email = form["Email"]
        sign_username = form["Username"]
        sign_pass = form["Password"]
        u_list = find_username(sign_username)
        if u_list == None:
            # if sign_email == None or sign_username == None or sign_pass == None:
            #     return "Nhap day du du lieu"
            # else:
            signup_db(sign_name,sign_l_name,sign_email,sign_username,sign_pass)
            return "Tao Tai Khoan Thanh Cong"
            
        else:
            return "Nguoi Dung da ton tai"
           

@app.route("/post")
def new_post():
    if "token" in session:
        # if request.method == "GET":
        #     return render_template("post.html")
        # elif request.method == "POST":
        #     form = request.form
        #     n = form["place"]
        #     p = form["content"]
        return render_template("post.html")
    else:
        return "Please login!"

    

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/logout")
def logout():
    del session["token"]
    return redirect("/login")


@app.route('/uploader', methods = ['GET', 'POST'])
def upload_file_page():
   return render_template('upload.html')

if __name__ == '__main__':
   app.run(debug = True)