from flask import render_template, redirect, url_for, flash
from app import app, db, bcrypt
from app.forms import LoginForm, RegistrationForm
from app.models import User
from flask_login import login_user


@app.route('/')
def home():
    return render_template('home.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user)
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check email and password', 'danger')
    return render_template('login.html', form=form)



@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        # Hash de la contraseña
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        
        # Crear el usuario
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        
        # Guardar en la base de datos
        db.session.add(user)
        db.session.commit()
        
        flash('Account created successfully! You can now log in.', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', form=form)
