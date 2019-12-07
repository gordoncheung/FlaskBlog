from flaskblog import db, login_manager
from datetime import datetime
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    # We will hash password so we don't store as plaintext
    password = db.Column(db.String(60), nullable=False)
    # lazy means sqlalchemy will load data in one go
    # backref means that post will be able to reference author to get the user that created it
    # this will be an additional query that grabs every post associated to the user
    posts = db.relationship('Post', backref='author', lazy=True)

    # double underscore method is magic method
    # how our object is printed when we print it out
    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.image_file}')";

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    # note that utcnow has no parenthesis because we are passing the function not the result of the function
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)


    # double underscore method is magic method
    # how our object is printed when we print it out
    def __repr__(self):
        return f"Post('{self.title}', '{self.date_posted}')";
