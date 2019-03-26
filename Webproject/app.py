import os
from flask import Flask, flash, request, redirect, url_for, render_template, session, send_from_directory
from werkzeug.utils import secure_filename
from db import user
from bson import ObjectId

app = Flask(__name__)
app.config
app.config["SECRET_KEY"] = "@thanhinh1707abcdefghiklmn"


# Cấu hình thư mục, loại file upload
UPLOAD_FOLDER = 'C:/Users/NAM/Desktop/c4e26/WebProject/Webproject/static/img'
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS



# Trang chủ
@app.route("/")
def home_page():
    return render_template("index.html")


# Chức năng đăng ký cho người dùng
@app.route("/signup")
def sign_up():
    return render_template("signup.html")

# Chức năng login
def find_username(username):
    user_list = user.find_one({"username":username})
    return user_list

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

# Trang giới thiệu thành viên nhóm
@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/logout")
def logout():
    del session["token"]
    return redirect("/login")

# Chức năng uploader 
# @app.route('/uploader', methods = ['GET', 'POST'])
# def upload_file():
#     if request.method == 'GET':
#         return render_template("upload.html")

#     if request.method == 'POST':
#         # check if the post request has the file part
#         if 'file' not in request.files:
#             flash('No file part')
#             return redirect(request.url)
#         file = request.files['file']
#         # if user does not select file, browser also
#         # submit a empty part without filename
#         if file.filename == '':
#             flash('No selected file')
#             return redirect(request.url)
#         if file and allowed_file(file.filename):
#             filename = secure_filename(file.filename)
#             file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
#     return "Uploaded"


@app.route('/post', methods = ['GET', 'POST'])
def new_post():
    return render_template("post.html")

def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'],filename)
def upload_file():
    if request.method == 'GET':
        return render_template("post.html")

    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # if user does not select file, browser also
        # submit a empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
    return ("/post")

        
        

if __name__ == '__main__':
   app.run(debug = True)