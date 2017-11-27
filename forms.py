from flask_wtf import Form
from wtforms import PasswordField
from wtforms import SubmitField
from wtforms.fields.html5 import EmailField
from wtforms import validators
from wtforms import TextField, StringField, TextAreaField

from wtforms.widgets import TextArea

class RegistrationForm(Form):
	email = EmailField('email', validators=[validators.DataRequired(), validators.Email()])
	password = PasswordField('password', validators = [validators.DataRequired(), validators.Length(min=8, message='Пароль должен состоять минимум из 8 символов')])
	password2 = PasswordField('password2', validators=[validators.DataRequired(), validators.EqualTo('password', message='Пароли должны совпадать')])
	submit = SubmitField('submit', [validators.DataRequired()])
	
class LoginForm(Form):
	loginemail = EmailField('email', validators=[validators.DataRequired(), validators.Email()])
	loginpassword = PasswordField('password', validators = [validators.DataRequired(message='Password Field is required')])
	submit = SubmitField('submit', [validators.DataRequired()])

class CreateMessageForm(Form):
	reciever = TextField('reciever', validators=[validators.DataRequired()])
	message = TextAreaField('message', validators=[validators.DataRequired()])
	submit = SubmitField('createmessagesubmit', validators=[validators.DataRequired()])