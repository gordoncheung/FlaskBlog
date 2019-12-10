import os
import secrets
from PIL import Image
from flask import url_for, current_app
from flask_mail import Message
from flaskblog import mail

# considerations - we should resize the image that we are saving before we commit
# to the file system as images can be big
# to do this we leverage Pillow library (PIL) import
def save_picture(form_picture):
    # we should save the filename as random because it may collide with our existing files
    # utilizing secrets
    random_hex = secrets.token_hex(8)
    # need to get the file extension
    f_name, f_ext = os.path.splitext(form_picture.filename)
    # you can throw away variable name f_name by putting an underscore instead
    picture_fn = random_hex + f_ext
    picture_path = os.path.join(current_app.root_path, 'static/profile_pics', picture_fn)

    output_size = (125, 125)
    i = Image.open(form_picture)
    i.thumbnail(output_size)

    # commit to file system
    i.save(picture_path)

    i.close()

    return picture_fn


def send_reset_email(user):
    token = user.get_reset_token()
    # do not spoof a sender otherwise you will end up in spam folder
    msg = Message('Password Reset Request', 
                    sender='itsgordonlol@gmail.com', 
                    recipients=[user.email])
    # _external=true gives an absolute URL instead of a relative. So this gives the full url_for
    msg.body = f'''To reset your password, visit the following link:
{url_for('reset_token', token=token, _external=True)}

If you did not make this request then simply ignore this email and no change will be made
'''
    mail.send(msg)