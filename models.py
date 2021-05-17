# define database models
# database models for users and database models for notes
from . import db
# import from current package(webside folder) db object
from flask_login import UserMixin
# user object needs to inherit from UserMixin
from sqlalchemy.sql import func

class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(10000))
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    # allow to assosiate a note with a user
    # assosiate different information with different users
    # setup a relationship between a user and node (foreign key - column that reference to a column of another column of database )
    # we need this because one user can have many notes
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    



class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email =db.Column(db.String(150), unique=True)
    password =db.Column(db.String(150))
    first_name =db.Column(db.String(150))
    # we need to be able all users to find all their notes
    # do your magic and every time you create a note 
    # add into this users notes relationship that note.id  
    notes = db.relationship('Note') # this would be a list that would stote all the different notes
    # when you do the foreign key you do a lower case ( str 17), when you do the relationship you referencing the name of the class (which is obviosly capital)
