from flask import Flask
from flask import redirect
from flask import url_for
from flask import request
from flask import render_template

from flask.ext.login import LoginManager
from flask.ext.login import login_required
from flask.ext.login import login_user
from flask.ext.login import logout_user
from flask.ext.login import current_user

#from mockdbhelper import MockDBHelper as DBHelper
from passwordhelper import PasswordHelper
from user import User
from forms import RegistrationForm, LoginForm, CreateMessageForm

import rsa_engine
import config 

if config.test:
	from mockdbhelper import MockDBHelper as DBHelper
else:
	from dbhelper import DBHelper

DB = DBHelper()
PH = PasswordHelper()

app = Flask(__name__)
app.secret_key = 'tPXJY3X37Qybz4QykV+hOyUxVQeEXf1Ao2C8upz+fGQXKsM'
login_manager = LoginManager(app)


@app.route('/')
def home():
	return(render_template('home.html', loginform=LoginForm(), registrationform = RegistrationForm()))
	
@app.route('/register', methods=['POST'])
def register():
	form = RegistrationForm(request.form)
	if form.validate():
		if DB.get_user(form.email.data):
			form.email.errors.append("Адрес уже зарегистрирован")
			return(render_template('home.html', loginform=LoginForm(), registrationform = form ))
		salt = PH.get_salt()
		hashed = PH.get_hash(form.password2.data + salt)
		pub_key, priv_key = rsa_engine.create_keys(form.email.data)
		DB.add_user(form.email.data, salt, hashed, pub_key, priv_key)
		return(render_template('home.html', loginform=LoginForm(), registrationform=form, onloadmessage='Регистрация прошла успешно! Войдите в систему.'))
	return(render_template('home.html', loginform=LoginForm(), registrationform=form))
	
@app.route('/login', methods=['POST'])
def login():
	form = LoginForm(request.form)
	if form.validate():
		stored_user = DB.get_user(form.loginemail.data)
		if stored_user and PH.validate_password(form.loginpassword.data, stored_user['salt'], stored_user['hashed']):
			user = User(form.loginemail.data)
			login_user(user, remember=True)
			return(redirect(url_for('account')))
		form.loginemail.errors.append('Email или пароль не действительные')
	return(render_template('home.html', loginform=form, registrationform=RegistrationForm()))

@app.route('/logout')
def logout():
	logout_user()
	return(redirect(url_for('home')))

@login_manager.user_loader
def load_user(user_id):
	user_password = DB.get_user(user_id)
	if user_password:
		return(User(user_id))

@app.route('/account')
@login_required
def account():
	messages = DB.get_messages(current_user.get_id())
	return(render_template('account.html', createmessageform=CreateMessageForm(), messages=messages))
	
@app.route('/account/createmessage', methods=['POST'])
@login_required
def account_createmessage():
	form=CreateMessageForm(request.form)
	if form.validate():
		reciever = form.reciever.data
		message = form.message.data
		pubkey = DB.get_pubkey(reciever)
		enc_message = rsa_engine.encrypt_message(reciever, message, pubkey)
		messageid = DB.add_message(reciever, message, enc_message, current_user.get_id())
		return(redirect(url_for('account')))
	return(render_template('account.html', createmessageform=form,messages=DB.get_messages(current_user.get_id())))


@app.route('/dashboard')
@login_required
def dashboard():
	messages = DB.get_dashboard_messages(current_user.get_id())
	return(render_template('dashboard.html', messages=messages))
	

if __name__ == '__main__':
	app.run(port=5000, debug=True)
	
	
