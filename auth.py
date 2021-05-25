from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User
# few things from flask login that will allow to hash a password
# sequre the password  - change the password (or convert the password)
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        # looking for a specific entry in your database (for the first entry of the email)
        user = User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password, password):
                flash('Logged in successfully!', category ='success')
            else: 
                flash('Incorrect password, try again.', category='error')
        else:
            flash('Email does not exist.', category='error')
    return render_template("login.html", boolean = False,text="Testing", user="Kathy")

@auth.route('/logout')
def logout():
    return "<p>logout</p>"

@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    data = request.form
    print(data)
    # get all of the information from my forms
    
    if request.method == 'POST':
        email = request.form.get('email')
        print("email", email)
        first_name = request.form.get('first_name')
        print("first name", first_name)
        password1 = request.form.get('password1')
        print("password1", password1)
        password2 = request.form.get('password2')
        print("password2", password2)

        user = User.query.filter_by(email=email).first()
        if user:
            flash('Email already exists.', category='error')
        elif len(email) < 4:
            print("Email must be greater that 3 characters")
            flash('Email must be greater than 3 characters', category='error')
        elif len(first_name) < 2:
            flash('First name must be greater than 1 characters', category='error')
        elif password1 != password2:
            flash('Passwords don\'t match.', category='error')
        elif len(password1) < 7:
            flash('Password must be at least 7 characters.', category='error')
        else:
            # create a new user
            new_user = User(email=email, first_name=first_name, password=generate_password_hash(password1, method='sha256'))            
            # add account to the database
            db.session.add(new_user)
            db.session.commit()

            # add user to the database
            flash('Account created', category='success')
            print("Account created!")
            # redirect user to the home page 
            return redirect(url_for('views.home'))

    return render_template("sign_up.html")
        