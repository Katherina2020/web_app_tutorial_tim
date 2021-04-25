from flask import Blueprint, render_template

views = Blueprint('views', __name__)

# going to the main page of our website
@views.route('/')
def home():
    return render_template("home.html")
    