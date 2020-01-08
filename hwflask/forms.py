from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, EqualTo
from flask_wtf import FlaskForm

class SignupForm(FlaskForm):
    avengername = StringField("AvengerName", validators=[DataRequired()])
    phonenumber = StringField("Phone Number", validators=[DataRequired()])
    address = StringField("Address", validators=[DataRequired()])
    submit = SubmitField("Submit")