import os
from flask import Flask, flash, request, redirect, url_for, render_template, session
from db import *
from bson import ObjectId
from connect import signup_db
import random
from up_user import add_user_post
#from db import post_collection,user
from deff import *
app = Flask(__name__)

app.config["SECRET_KEY"] = "@thanhinh1707abcdefghiklmn"

def find_username(username):
    user_list = user_collection.find_one({"Username":username})
    return user_list

def find_user_post(username):
    user_post_list = user_post.find({"Username":username})
    post_list_user = []
    for post in user_post_list:
        post_list_user.append(post)
    return post_list_user


@app.route("/")
def home_page():
    user_post_li=user_post.find().sort([("_id", -1), ("date", -1)])
    post_list = []
    for i in user_post_li:
        post_list.append(i)
    post_list_ = post_list
    return render_template("index.html", post_list_ = post_list_)

@app.route("/about")
def about():
    return render_template("about.html")
    
@app.route("/detail/<int:index>")
def image1(index):
    post_detail = post_list[index]
    return render_template("image1.html",post_detail = post_detail)



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
            return render_template("login_error.html")
        elif u_list["Password"] != p:
            return render_template("login_error.html")
        else:
            # id_user = u_list["_id"]
            session["token"] = u
            session['logged_in'] = True
            # a = session["token"]
            return  render_template("index.html")
        

@app.route("/logout")
def logout():
    session.pop('logged_in', None)
    return render_template("index.html")



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
        sign_address = form["Address"]
        u_list = find_username(sign_username)
        if u_list == None:
            # if sign_email == None or sign_username == None or sign_pass == None:
            #     return "Nhap day du du lieu"
            # else:
            signup_db(sign_name,sign_l_name,sign_email,sign_username,sign_pass,sign_address)
            return render_template("login.html")
            
        else:
            return render_template("signup_error.html")
           

@app.route("/post", methods = ["GET", "POST"])
def new_post():
    if "token" in session:
        
        if request.method == "POST":
            form = request.form
            Title = form["Title"]
            username = session["token"]
            Location = form["Location"]
            Name = form["Content"]
            Vehicle = form["Vehicle"]
            img_list = []
            img_file = request.form['base64']
            img_list.append(img_file)
            tipsfortravel = ["tipsfortravel"]
            if Title != None:               
                
                add_user_post(Title,username,img_list,Name,Location,Vehicle,tipsfortravel)
                return render_template("Dashboard.html")
            else:
                return "Need Title"
        else:
            return render_template("post.html")
    else:
        return render_template("login.html")
        




@app.route('/uploader', methods = ['GET', 'POST'])
def upload_file_page():
   return render_template('upload.html')

@app.route("/Dashboard")
def Dashboard():
    if "token" in session:
        username = session["token"]
        list_user_p = find_user_post(username)
        # len_list = len(list_user_p)
        return render_template("Dashboard.html",list_user_p=list_user_p)
    else:
        return "Need login first"
@app.route("/dashboard/<int:index>")
def dashboard_indx(index):
    username = session["token"]
    list_user_p = find_user_post(username)
    dashboard_detail = list_user_p[index]
    return render_template("image3.html",post_detail = dashboard_detail)


if __name__ == '__main__':
   app.run(debug = True)