from flask import Flask

app= Flask(__name__)

@app.route('/')
def hello_world():
    return '<h1>    CODING IS PURE MATHEMATICS ! </h1>'

@app.route('/about')
def about_page():
    return '<h1> About Page </h1>'

@app.route('/admin')
def admin_page():
    return '<h1> Admin Page </h1>'