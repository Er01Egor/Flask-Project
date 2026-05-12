from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, SubmitField, EmailField
from wtforms.validators import DataRequired, Email, EqualTo

class RegisterForm(FlaskForm):
    pass

class LoginForm(FlaskForm):
    pass