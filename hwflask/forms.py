from wtforms import StringField, SubmitField, PasswordField, TextAreaField
from wtforms.validators import DataRequired, EqualTo, Email, length
from flask_wtf import FlaskForm

class SignupForm(FlaskForm):
    avengername = StringField("AvengerName", validators=[DataRequired(),])
    phonenumber = StringField("Phone Number", validators=[DataRequired()])
    address = StringField("Address", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    confirm_pass = PasswordField("Confirm Password", validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField("Submit")

class LoginForm(FlaskForm):
    avengername = StringField("AvengerName", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    submit = SubmitField("Submit")

class PostForm(FlaskForm):
    title = StringField("Title", validators=[DataRequired()])
    content = TextAreaField("Content", validators=[DataRequired(), length(max=300)])
    submit = SubmitField("Submit")