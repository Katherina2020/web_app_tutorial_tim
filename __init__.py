# this file would do website folder a python package
from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'hfyfik gfkukf'

    # register blueprint into init.py
    # we have a blueprint that is containing some 
    # some different views of a application
    # here is where they are
    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')
    
    return app
