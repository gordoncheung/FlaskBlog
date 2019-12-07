from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager # Session handler
# Anytime you import anything from a module, it runs all the code in the module

app = Flask(__name__)
app.config['SECRET_KEY'] = '21641a34cd7bc1d3f0ed98266c8d3794'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
# Pass function name login() to the login_view
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'

from flaskblog import routes