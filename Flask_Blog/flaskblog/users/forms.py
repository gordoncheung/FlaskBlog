from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from flask_login import current_user
from flaskblog.models import User

# Inheritance in Python is done in this manner. 
# RegistrationForm is inheriting from FlaskForm
class RegistrationForm(FlaskForm):
    # the string is the label in HTML
    username = StringField('Username', 
                            validators=[DataRequired(), 
                            Length(min=2, max=20)]) 
    email = StringField('Email',
                        validators=[DataRequired(),
                        Email()
                        ])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')

    # Validation function to check if user already exists with the name
    def validate_username(self, username):
        # username.data is the thing that comes from the form
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('Username already exists.')
        
    def validate_email(self, email):
        email = User.query.filter_by(email=email.data).first()
        if email:
            raise ValidationError('Email already exists.')

class LoginForm(FlaskForm):
    # the string is the label in HTML
    email = StringField('Email',
                        validators=[DataRequired(),
                        Email()
                        ])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')



class UpdateAccountForm(FlaskForm):
    # the string is the label in HTML
    username = StringField('Username', 
                            validators=[DataRequired(), 
                            Length(min=2, max=20)]) 
    email = StringField('Email',
                        validators=[DataRequired(),
                        Email()
                        ])
    picture = FileField('Update Profile Picture', validators=[FileAllowed(['jpg','png'])])
    address = TextAreaField('Address', validators=[Length(max=200)])
    submit = SubmitField('Update')

    # Validation function to check if user already exists with the name
    def validate_username(self, username):
        if username.data != current_user.username:
            # username.data is the thing that comes from the form
            user = User.query.filter_by(username=username.data).first()
            if user:
                raise ValidationError('Username already exists.')
        
    def validate_email(self, email):
        if email.data != current_user.email:
            email = User.query.filter_by(email=email.data).first()
            if email:
                raise ValidationError('Email already exists.')


class RequestResetForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    submit = SubmitField('Request Password Reset')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is None:
            ValidationError('There is no account with the specified email.')


class ResetPasswordForm(FlaskForm):
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Reset Password')