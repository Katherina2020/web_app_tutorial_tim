# This file stores standart routs for our website that are not related to authentication 
from flask import Blueprint, render_template, request, flash
from flask_login import login_required, current_user
from .models import Note
from . import db

views = Blueprint('views', __name__)

# going to the main page of our website
@views.route('/', methods=['GET','POST'])
@login_required     # now you can't go to the home page if you are not logged in
def home():
    if request.method == 'POST':
        note = request.form.get('note')

        if len(note) < 1:
            flash('Note is too short!', category='error')
        else:
            # create note
            new_note = Note(data=note, user_id=current_user.id)
            db.session.add(new_note)
            db.session.commit()
            flash('Note added!', category='success')

    # user=current_user means that we will be able in a template reference this current user if it's authentificated
    return render_template("home.html", user=current_user)
    