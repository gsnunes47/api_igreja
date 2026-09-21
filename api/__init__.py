from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bcrypt import Bcrypt
from datetime import timedelta

app = Flask('__main__', template_folder=r'sistema_igreja\templates')
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://usuario:senha@host/banco'
app.config['SECRET_KEY'] = 'chave-local'

database = SQLAlchemy(app)
login_manager = LoginManager(app)
bcrypt = Bcrypt(app)

from api import routes
