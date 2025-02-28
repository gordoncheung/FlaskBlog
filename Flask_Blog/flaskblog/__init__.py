from flaskblog.config import Config
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager # Session handler
from flask_mail import Mail
from flask_socketio import SocketIO
# Anytime you import anything from a module, it runs all the code in the module


#app.config['SECRET_KEY'] = '21641a34cd7bc1d3f0ed98266c8d3794'
#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
#db = SQLAlchemy(app)
#bcrypt = Bcrypt(app)
#login_manager = LoginManager(app)
db = SQLAlchemy()
bcrypt = Bcrypt()
socketio = SocketIO()
login_manager = LoginManager()
# Pass function name login() to the login_view
login_manager.login_view = 'users.login'
login_manager.login_message_category = 'info'
#app.config['MAIL_SERVER'] = 'smtp.googlemail.com'
#app.config['MAIL_PORT'] = 587
#app.config['MAIL_USE_TLS'] = True
#mail = Mail(app)
mail = Mail()


# ability to init app with diff configurations, e.g. sandbox or prod
def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)
    mail.init_app(app)
    socketio.init_app(app)

    from flaskblog.users.routes import users
    from flaskblog.posts.routes import posts
    from flaskblog.main.routes import main
    from flaskblog.errors.handlers import errors
    from flaskblog.chat.routes import chat

    app.register_blueprint(chat)
    app.register_blueprint(users)
    app.register_blueprint(posts)
    app.register_blueprint(main)
    app.register_blueprint(errors)

    from flask_googlemaps import GoogleMaps
    GoogleMaps(app)

    return app