from flask import Flask, render_template

app= Flask(__name__)

@app.route('/')
@app.route('/home')
def home_page():
    return render_template('home.html')

@app.route('/admin')
def admin_page():
    item = [
        {'id': 1, 'date': '20/12/2022', 'name': 'Evaline', 'kilograms': '1200', 'amount': 9600},
        {'id': 2, 'date': '20/12/2022', 'name': 'Leonard', 'kilograms': '1300', 'amount': 10400},
        {'id': 3, 'date': '20/12/2022', 'name': 'Karen', 'kilograms': '1400', 'amount': 11200}
    ]
    return render_template('admin.html', items=item)