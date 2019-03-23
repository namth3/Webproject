import os
from flask import Flask, flash, request, redirect, url_for, render_template, session
from flask_pymongo import PyMongo
from werkzeug.utils import secure_filename
from db import user
from bson import ObjectId


app = Flask(__name__)
app.config
app.config["SECRET_KEY"] = "@thanhinh1707abcdefghiklmn"
APP_ROOT = os.path.dirname(os.path.abspath(__file__))

@app.route("/")
def home_page():
    return render_template("index.html")

@app.route("/post")
def new_post():
    return render_template("post.html")

@app.route("/signup")
def sign_up():
    return render_template("signup.html")

@app.route("/login")

def find_username(username):
    user_list = user.find({"username": username})
    return user_list

def login():
    if request.method == "GET":
        return render_template("login.html")
    elif request.method == "POST":
        form = request.form
        u = form["user"]
        p = form["password"]
        u_list = find_username(u)
        if u_list == None:
            return "No such user"
        elif u_list["password"] != p:
            return "Wrong password"
        else:
            session["token"] = u
            return  redirect("/post")
@app.route("/logout")

def logout():
    del session["token"]
    return redirect("/login")


@app.route('/uploader', methods = ['GET', 'POST'])

def upload_file_page():
   return render_template('upload.html')

if __name__ == '__main__':
   app.run(debug = True)