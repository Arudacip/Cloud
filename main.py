import os
import logging
import redis
import gevent
from flask import Flask, render_template
from flask_sockets import Sockets

app = Flask(__name__)
app.debug = 'DEBUG' in os.environ

sockets = Sockets(app)
#chats = ChatBackend(app, redis, REDIS_CHAN)

@app.route('/')
def hello():
    return render_template('myApp/FrontEnd/HTML/static/index.html')