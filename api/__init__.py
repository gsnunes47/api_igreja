from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask('__main__', template_folder=r'sistema_igreja\templates')
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://membros_user:vwSkzYDECJ6JTpCo05tZJa7dDqUbCVi7@dpg-cmqg10mg1b2c73d5nv3g-a/membros'

database = SQLAlchemy(app)

from api import routes
