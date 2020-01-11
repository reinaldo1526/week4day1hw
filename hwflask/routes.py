from hwflask import app, db 
from flask import render_template, request, redirect, url_for
from hwflask.forms import SignupForm,LoginForm,PostForm

from werkzeug.security import check_password_hash

from flask_login import login_user, current_user,login_required

from hwflask.models import User,Post
# Home Route
@app.route("/")
def home():
    posts = Post.query.all()
    return render_template("home.html", post = posts)

    # Sign Up Route
@app.route("/signup", methods=["GET", "POST"])
def signup():
    signupForm = SignupForm()
    if request.method == "POST":
        avengername = signupForm.avengername.data
        address = signupForm.address.data
        phonenumber = signupForm.phonenumber.data
        password = signupForm.password.data
        print(avengername, address, phonenumber,password)

        user = User(avengername, address,password)
        db.session.add(user)
        db.session.commit()
    return render_template("signup.html", signupform = signupForm)


#login route
@app.route("/login", methods=["GET", "POST"])
def login():
    loginForm = LoginForm()
    if request.method == "POST":
        user_avengername = loginForm.avengername.data
        password = loginForm.password.data
        # find out who the logged in user currently is
        logged_user = User.query.filter(User.avengername == user_avengername).first()
        if logged_user and check_password_hash(logged_user.password,password):
            login_user(logged_user)
            print(current_user.avengername)
            return redirect(url_for('home'))
        else:
            print("Not Valid Method")
    return render_template("login.html", loginform = loginForm)

@app.route("/post", methods = ["GET", "POST"])
@login_required
def post():
    postForm = PostForm()
    title = postForm.title.data
    content = postForm.content.data
    user_id = current_user.id
    print(title,content,user_id)

    # Saving Post Data to Database
    post = Post(title = title, content = content, user_id = user_id)
    db.session.add(post)
    db.session.commit()

    return render_template('create_post.html', postform = postForm)


