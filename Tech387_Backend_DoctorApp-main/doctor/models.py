from doctor import db, login_manager, bcrypt
from flask_login import UserMixin


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

#I will define two classes User and Patient and define function load_user thar returns User instance 
#based on the provided user_id
#Methods for password hashing and checking


#The model class User inherits from db.Model and UserMixin
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.String(length=30), nullable=False, unique=True)
    email_address = db.Column(db.String(length=50), nullable=False, unique=True)
    password_hash = db.Column(db.String(), nullable=False)
    #relationship with Patient through the patients attribute
    patients = db.relationship('Patient', backref='doctor', lazy=True)

    @property
    def password(self):
        return self.password_hash

    @password.setter
    def password(self, plain_text_password):
        self.password_hash = bcrypt.generate_password_hash(plain_text_password).decode('utf-8')

    def check_password_correction(self, attempted_password):
        return bcrypt.check_password_hash(self.password_hash, attempted_password)


class Patient(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.String(length=30), nullable=False, unique=True)
    disease = db.Column(db.String(length=50), nullable=False)
    time = db.Column(db.String(), nullable=False)
    doctor_id = db.Column(db.Integer(), db.ForeignKey('user.id'))
