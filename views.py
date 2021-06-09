# This file stores standart routs for our website that are not related to authentication 
from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user
from .models import Note
from . import db
import json

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
    
    @views.route('/delete-note', methods=['POST'])
    def delete_note():
        print("delete_note called")
        # look for the note id that was sent to us
        # a request will come in a data parameter of our 
        # request object which we need load as a JSON
        # take a request data which is a string
        # this string is what we were sent from 
        # index.js  noteId: noteId
        # and turn this string into a python dictionary object
        note = json.loads(request.data)
        # so we can access noteId attribute
        noteId = note['noteId']
        print(noteId,"noteId")
        
        # and than find this note that has this id
        note = Note.query.get(noteId)
        # if note exist:
        if note:
            # if user own this note he will delete it
            if note.user_id == current_user.id:
                print("current user id: ", current_user.id)
                db.session.delete(note)
                db.session.commit()
        # return an empty response
        return jsonify({})
