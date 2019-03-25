import os
from flask import Flask, flash, request, redirect, url_for, render_template, session
from db import user
from bson import ObjectId


app = Flask(__name__)
app.config
app.config["SECRET_KEY"] = "@thanhinh1707abcdefghiklmn"



def find_username(username):
    user_list = user.find_one({"username":username})
    return user_list


@app.route("/")
def home_page():
    return render_template("index.html")



@app.route("/signup")
def sign_up():
    return render_template("signup.html")

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
        elif u_list["password"] != p:
            return "Wrong password"
        else:
            session["token"] = u
            return  redirect("/")


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