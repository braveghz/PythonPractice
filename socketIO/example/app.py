#!/usr/bin/env python
# -*- coding:utf-8 -*-


from flask import Flask, render_template, session, request
from flask_socketio import SocketIO, emit

app = Flask(__name__, template_folder='./')
app.config['SECRET_KEY'] = 'secret!'

socketio = SocketIO(app)


@app.route('/')
def index():
    return render_template('index.html')

# on装饰器 监听
# 发送消息：未命名事件用send()，已命名事件用emit()


@socketio.on('connect_event')  # 处理收到的 connect_event 事件
def connected_msg(msg):
    emit('server_response', {'data': msg['data']})
    print msg['data']  # msg为 “connected！”


@socketio.on('client_event')  # 处理收到的client_event事件
def client_msg(msg):
    # 向客户端发送 server_response 事件，数据为msg
    emit('server_response', {'data': msg['data']})
    print msg['data']  # 可以在服务器端看到数据


if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=9999)
