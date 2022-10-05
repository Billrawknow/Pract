from datetime import date
from importlib import import_module
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime,date
from flask_bcrypt import Bcrypt

app= Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///pract.db'
app.config['SECRET_KEY']='0f896b6af276bca4b27ec1c2'

db=SQLAlchemy(app)
bcrypt = Bcrypt(app)

from pract import routes