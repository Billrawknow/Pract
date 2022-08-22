from pract import app
from flask import render_template,redirect, url_for

from pract.models import Item,User
from pract.forms import RegisterForm
from pract import db

@app.route('/')
@app.route('/home')
def home_page():
    return render_template('home.html')

@app.route('/admin')
def admin_page():
    item = Item.query.all()
    return render_template('admin.html', items=item)


@app.route('/register', methods=['GET', 'POST'])
def register_page():
    form = RegisterForm()
    if form.validate_on_submit():
        user_to_create = User(username=form.username.data,
                              email_address=form.email_address.data,
                              password_hash=form.password1.data)
        db.session.add(user_to_create)
        db.session.commit()
        return redirect(url_for('admin_page'))
    return render_template('register.html', form=form)