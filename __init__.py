# this file would do website folder a python package
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager

db = SQLAlchemy()
DB_NAME ="database.db"

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'hfyfik gfkukf'
    # store the database in this website folder
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    # initialize database
    db.init_app(app)


    
    # register blueprint into init.py
    # we have a blueprint that is containing some 
    # some different views of a application
    # here is where they are
    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')
    
    from .models import User, Note

    create_database(app)

    login_manager = LoginManager()
    # where flask should redirect us if user is not logged if
    login_manager.login_view = 'auth.login'
    # telling to logging_manager which app we are using
    login_manager.init_app(app)

    # tell flask what user we are looking for
    # looking for a user module and we are going refference them by id
    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))
   

    return app

def create_database(app):
    if not path.exists('website/' + DB_NAME):
        db.create_all(app=app)
        print('Created Database!')
