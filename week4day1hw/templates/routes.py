from week4day1hw import app 
from flask import render_template

# Home Route
@app.route("/")
def home():
    return render_template("home.html")