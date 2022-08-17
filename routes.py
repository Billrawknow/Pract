      
@app.route('/')
@app.route('/home')
def home_page():
    return render_template('home.html')

@app.route('/admin')
def admin_page():
    item = Item.query.all()
    return render_template('admin.html', items=item)