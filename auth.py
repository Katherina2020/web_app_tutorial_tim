from flask import Blueprint, render_template, request, flash

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
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
        firstName = request.form.get('firstName')
        print("first name", firstName)
        password1 = request.form.get('password1')
        print("password1", password1)
        password2 = request.form.get('password2')
        print("password2", password2)

        if len(email) < 10:
            print("Email must be greater that 4 characters")
            flash('Email must be greater than 4 characters', category='error')
        elif len(firstName) < 2:
            pass
        else:
            print("Account created!")
    return render_template("sign_up.html")
        