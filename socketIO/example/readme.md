## Flask-SocketIO

Flask-Socketio是Socketio的Flask插件。Flask-Socketio基于异步处理各种事件：eventlet、gevent和Flask自带的Werkzeug，这些后面再说。

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

举个例子🌰

简单的 Flask-SocketIO 应用

app.py + index.html

```
# 运行
python app.py
```

小栗子可以直接跑一下，就看懂了
