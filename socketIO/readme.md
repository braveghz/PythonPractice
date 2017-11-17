# Flask+WebSocket

socketIO 学习😝


## Flask-SocketIO

Flask-Socketio是Socketio的Flask插件。

Flask-Socketio基于异步处理各种事件：eventlet、gevent和Flask自带的Werkzeug，这些后面再说。

安装

```
pip install flask-socketio
```

初始化

```
from flask import Flask, render_template
from flask_socketio import SocketIO

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

if __name__ == '__main__':
    socketio.run(app)
```

SocketIO 使用 event 表示客户端和服务端接受到的消息。

客户端使用 Javascript 回调函数处理。

服务器端使用注册函数来处理事件。

举个栗子 🌰 看example

-----

### 相关文档

[WebSocket](https://developer.mozilla.org/zh-CN/docs/Web/API/WebSocket)

[flask-socketio中文文档](http://www.hi-roy.com/2015/12/29/flask-socketio%E4%B8%AD%E6%96%87%E6%96%87%E6%A1%A3/)


