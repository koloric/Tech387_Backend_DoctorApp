
#Importing Required Libraries and Models:
from doctor import app, db
from doctor.forms import LoginForm
from doctor.models import User, Patient
from flask import render_template, redirect, url_for, flash
from flask_login import login_user, logout_user, login_required, current_user
from datetime import datetime, timedelta
from flask import json


# Routes

#Login Route
@app.route('/', methods=['GET', 'POST'])
@app.route('/login', methods=['GET', 'POST'])
def login_page():
    form = LoginForm()
    if form.validate_on_submit():
        attempted_user = User.query.filter_by(email_address=form.email.data).first()
        if attempted_user and attempted_user.check_password_correction(attempted_password=form.password.data):
            login_user(attempted_user)
            flash(f'Uspjesno ste se logovali: {attempted_user.fullname} ', category='success')
            return redirect(url_for('home_page'))
        else:
            flash(f'Pogresan e-mail ili password', category='danger')
    return render_template('login.html', form=form)

#Home Route

@app.route('/home', methods=['GET', 'POST'])
@login_required
def home_page():
    patients = Patient.query.filter_by(doctor=current_user.id)
    for patient in patients:
        patient.time = convert_to_date(patient.time)
        patient.scheduled = check_scheduled(patient.time)
    return render_template('home.html', patients=patients)

#Logout Route

@app.route('/logout')
def logout_page():
    logout_user()
    flash("You have been logged out!", category='info')
    return redirect(url_for("login_page"))


# Error Handlers
@app.errorhandler(HTTPException)
def handler_exception(e):
    response = e.get_response()
    response.data = json.dumps({key: getattr(e, key) for key in ['code', 'name', 'description']})
    response.content_type = "application/json"
    return response


# Datetime functions
def convert_to_date(date):
    return datetime.fromtimestamp(int(date))


def check_scheduled(date):
    date_now = str(datetime.now()).split()[0]
    date_scheduled = str(date).split()[0]
    date_tomorrow = str(datetime.now() + timedelta(1)).split()[0]

    if date_now == date_scheduled:
        return "Today"
    elif date_tomorrow == date_scheduled:
        return "Tomorrow"
    else:
        return date_scheduled
