from flask import render_template, Blueprint
from flaskblog import socketio
from flask_login import current_user, login_required

chat = Blueprint('chat', __name__)

@chat.route('/chat')
@login_required
def sessions():
    return render_template('chat.html')

def messageReceived(methods=['GET', 'POST']):
    print('message was received!!!')

@socketio.on('my event')
def handle_my_custom_event(json, methods=['GET', 'POST']):
    print('received my event: ' + str(json))
    socketio.emit('my response', json, callback=messageReceived)