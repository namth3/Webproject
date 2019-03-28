import os
from flask import Flask, flash, request, redirect, url_for, render_template, session
from db import *
from bson import ObjectId
from connect import signup_db
#from db import post_collection,user
from deff import *
app = Flask(__name__)
app.config
app.config["SECRET_KEY"] = "@thanhinh1707abcdefghiklmn"



def find_username(username):
    user_list = user_collection.find_one({"Username":username})
    return user_list

@app.route("/")
def home_page():
    return render_template("index.html",a=a,b=b,c=c,d=d,e=e)


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
            id_user = u_list["_id"]
            session["token"] = u
            a = session["token"]
            return  redirect(''),

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
    return render_template("post.html")

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