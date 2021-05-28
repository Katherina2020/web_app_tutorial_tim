# This file stores standart routs for our website that are not related to authentication 
from flask import Blueprint, render_template
from flask_login import login_required, current_user

views = Blueprint('views', __name__)

# going to the main page of our website
@views.route('/')
@login_required     # now you can't go to the home page if you are not logged in
def home():
    # user=current_user means that we will be able in a template reference this current user if it's authentificated
    return render_template("home.html", user=current_user)
    