from market import app
from flask import render_template, redirect, url_for
from market.models import Item, User
from market.forms import RegisterForm
from market import db
from flask_login import login_user, logout_user, login_required

@app.route('/')
@app.route('/home')#patirnt stranica
@login_required #možemo pristupiti pacijentima samo ako smo logobani
def home_page():
    return render_template('home.html')



@app.route('/register', methods=['GET', 'POST'])
def register_page():
    form = RegisterForm()
    if form.validate_on_submit():
        attempted_user = User.query.filter_by(email='career@tech387.com').first()
        if attempted_user and attempted_user.check_password_correction(
            attempted_password =="Pass123!"
        ):
            login_user(attempted_user)
            return redirect(url_for('home_page'))
        else: 
            flash('Pogresan email ili password')

    return render_template("login.html", form=form)

#ovdje sam nešto (svašta) zeznula. Ideja mi je bila referisati se na tabelu u bazi podataka i prepoynati ako su ti podaci uneseni
#da se korisnik odvede na stranicu sa pacijentima, ako ne onda da vrati na login stranicu. To bi bilo za slučaj poruke sa pogrešno unesenim podacima
#za ostala dva slučaja nisam sigurna, vjerovatno postoji neka šifra u sklopu insaliranih flask biblioteka (library) po kojoj se error prepoznaje


#Također, izvinjavam se na konfuznim varijablama koje su ostale iz flask projekta za vježbu. Nisam imala druge opcije nego odustati od inicijalnog koda jer nisam 
#mogla riješiti error(e), a izgubila sam previše vremena na tome. Katastrofa! Trebala sam odmag početi sa githubom da mogu pratit i dokumentovati promjene.
#base-zajedničko za sve stranice
#home-stranica sa pacijentima, kalendarima i vremenima (taj dio tablee u bazi podatak isto nije gotov)
#login-login

#ruta za logout


@app.route('/logout')
def logout_page():
    logout_user() #nova funkcija
    return redirect(url_for("register_page"))