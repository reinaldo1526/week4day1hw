from hwflask import app, db 
from flask import render_template, request, redirect, url_for
from hwflask.forms import SignupForm,LoginForm

from werkzeug.security import check_password_hash

from flask_login import login_user, current_user

from hwflask.models import User 

# Home Route
@app.route("/")
def home():
    return render_template("home.html")

    # Sign Up Route
@app.route("/signup", methods=["GET", "POST"])
def signup():
    if request .method == "POST":
        signupForm = SignupForm()
        avengername = signupForm.avengername.data
        address = signupForm.address.data
        phonenumber = signupForm.phonenumber.data
        password = signupForm.password.data
        print(avengername,address,phonenumber,password)

        user = User(avengername, address, phonenumber,password)
        db.session.add(user)
        db.session.commit()
    return render_template("signup.html", signupform = signupForm   )


#login route
@app.route("/login", methods=["GET", "POST"])
def login():
    loginForm = LoginForm()
    if request.method == "POST":
        user_email = loginForm.email.data
        password = loginForm.password.data
        # find out who the logged in user currently is
        logged_user = User.query.filter(User.email == user_email).first()
        if logged_user and check_password_hash(logged_user.password,password):
            login_user(logged_user)
            print(current_user.username)
            return redirect(url_for('home'))
        else:
            print("Not Valid Method")
    return render_template("login.html", loginform = loginForm)

