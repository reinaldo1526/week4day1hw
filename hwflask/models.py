from flask_sqlalchemy import SQLAlchemy
from hwflask import app,db 

from werkzeug.security import generate_password_hash

from datetime import datetime

#import user mixin
from hwflask import login
from flask_login import UserMixin

@login.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model,UserMixin):
    id = db.Column(db.Integer, primary_key = True)
    avengername = db.Column(db.String(150), nullable = False)
    email = db.Column(db.String(150), unique = True, nullable = False)
    password = db.Column(db.String(256), nullable = False)
    post = db.relationship('Post', backref = 'author', lazy = True)

    def __init__(self, avengername, email, password):
        self.avengername = avengername
        self.email = email
        self.password = self.set_password(password)

    def set_password(self, password):
        self.pw_hash = generate_password_hash(password, method = 'pbkdf2:sha256', salt_length=10)
        return self.pw_hash
    def __repr__(self):
        return '{} has been created' .format(self.avengername)

    class Post(db.Model):
        id = db.Column(db.Integer, primary_key = True)
        tittle = db.Column(db.String(200))
        content = db.Column(db.String(300))
        date_created = db.Column(db.DateTime, nullable = False, default = datetime.utcnow)
        user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable = False) 

        def __repr__(self):
            return "The title is {} and the user is {}".format(self.title,self.user_id)


