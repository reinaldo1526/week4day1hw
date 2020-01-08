from hwflask import app 
from flask import render_template
from hwflask.forms import SignupForm

# Home Route
@app.route("/")
def home():
    return render_template("home.html")

    # Sign Up Route
@app.route("/signup", methods=["GET", "POST"])
def signup():
    signupForm = SignupForm()
    avengername = signupForm.avengername.data
    address = signupForm.address.data
    phonenumber = signupForm.phonenumber.data
    print(avengername,address,phonenumber)
    return render_template("signup.html", signupform = signupForm   )