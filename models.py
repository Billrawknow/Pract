class Item(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    date = db.Column(db.String(10))
    name = db.Column(db.String(length=30), nullable=False, unique=True)
    kilograms = db.Column(db.Integer(), nullable=False)
    amount= db.Column(db.Integer(), nullable=False)


    def __repr__(self):
        return f'Item {self.name}'
        