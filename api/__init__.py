from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bcrypt import Bcrypt
from datetime import timedelta

app = Flask('__main__', template_folder=r'sistema_igreja\templates')
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://user:R67SICNGLtrJVGwYbySdZb6hUSLffm34@dpg-co23d3f79t8c73cgi3vg-a.oregon-postgres.render.com/membros_l0j3'
app.config['SECRET_KEY'] = 'chavesecreta'

database = SQLAlchemy(app)
login_manager = LoginManager(app)
bcrypt = Bcrypt(app)

from api import routes
