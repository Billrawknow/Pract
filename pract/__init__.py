from datetime import date
from importlib import import_module
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime,date
app= Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///pract.db'
db=SQLAlchemy(app)

from pract import routes