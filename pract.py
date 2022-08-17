from datetime import date
from importlib import import_module
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime,date


app= Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///pract.db'
db=SQLAlchemy(app)

class Item(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    date = db.Column(db.String(10))
    name = db.Column(db.String(length=30), nullable=False, unique=True)
    kilograms = db.Column(db.Integer(), nullable=False)
    amount= db.Column(db.Integer(), nullable=False)


    def __repr__(self):
        return f'Item {self.name}'
        
@app.route('/')
@app.route('/home')
def home_page():
    return render_template('home.html')

@app.route('/admin')
def admin_page():
    item = Item.query.all()
    return render_template('admin.html', items=item)