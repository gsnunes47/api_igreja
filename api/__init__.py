from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask('__main__', template_folder=r'sistema_igreja\templates')
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("DATABASE-URL")

database = SQLAlchemy(app)

from api import routes
