from pract import app
from flask import render_template
from pract.models import Item
from pract.forms import RegisterForm

@app.route('/')
@app.route('/home')
def home_page():
    return render_template('home.html')

@app.route('/admin')
def admin_page():
    item = Item.query.all()
    return render_template('admin.html', items=item)


@app.route('/register')
def register_page():
    form = RegisterForm()
    return render_template('register.html', form=form)