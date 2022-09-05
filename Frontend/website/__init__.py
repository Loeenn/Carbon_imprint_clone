import urllib
from urllib import parse
from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin

db = SQLAlchemy()


class Users(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(128), unique=True)
    password_hash = db.Column(db.String(256))
    first_name = db.Column(db.String(128))


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'hjshjhdjah kjshkjdhjaskdjlakjsdncjasds'

    params = urllib.parse.quote_plus(
        'DRIVER={SQL Server};SERVER=tcp:176.99.158.202;DATABASE=Carbon_imprint;UID=guest_carbon;PWD=asskarramba')
    app.config['SQLALCHEMY_DATABASE_URI'] = "mssql+pyodbc:///?odbc_connect=%s" % params
    db.init_app(app)

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login_register'
    login_manager.init_app(app)

    from .views import views
    from .auth import auth

    @login_manager.user_loader
    def load_user(id):
        return Users.query.get(int(id))

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    return app
