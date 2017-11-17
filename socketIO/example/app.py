#!/usr/bin/env python
from flask import Flask, render_template
from flask_socketio import SocketIO, emit

app = Flask(__name__, template_folder='./')
app.config['SECRET_KEY'] = 'secret!'

socketIo = SocketIO(app)


@app.route('/')
def index():
    return render_template('index.html')


@socketIo.on('connect_event')
def connected_msg(msg):
    emit('server_response', {'data': msg['data']})
    print (msg['data'])


@socketIo.on('client_event')
def client_msg(msg):
    emit('server_response', {'data': msg['data']})
    print (msg['data'])


if __name__ == '__main__':
    socketIo.run(app, host='127.0.0.1', port=9999)
