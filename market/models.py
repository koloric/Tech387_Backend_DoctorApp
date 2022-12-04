from market import db

class User(db.Model): #tačni podaci o passwordu i emailu
    id = db.Column(db.Integer(), primary_key=True)
    username = db.Column(db.String(length=30), nullable=False, unique=True)
    email_address = db.Column(db.String(length=50), nullable=False, unique=True)
    password= db.Column(db.String(length=60), nullable=False)

class Item(db.Model): #pacijenti (treba popuniti)
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(length=30), nullable=False, unique=True)
    time = db.Column()
    problem=db.Column(db.String(length=30), nullable=False, unique=True)