import os
import logging
import redis
import gevent
from flask import Flask, render_template
from flask_sockets import Sockets
from myApp.BackEnd.ChatBackEnd import ChatBackend

app = Flask(__name__)
app.debug = 'DEBUG' in os.environ

sockets = Sockets(app)

#chats = ChatBackend(app, redis, REDIS_CHAN)

@app.route('/')
def hello():
    return '<h3>HELLO WORLD!</h3>'#render_template('index.html')

'''@sockets.route('/submit')
def inbox(ws):
    """Receives incoming chat messages, inserts them into Redis."""
    while not ws.closed:
        # Sleep to prevent *contstant* context-switches.
        gevent.sleep(0.1)
        message = ws.receive()

        if message:
            app.logger.info(u'Inserting message: {}'.format(message))
            redis.publish(REDIS_CHAN, message)

@sockets.route('/receive')
def outbox(ws):
    """Sends outgoing chat messages, via `ChatBackend`."""
    chats.register(ws)
    while not ws.closed:
        # Context switch while `ChatBackend.start` is running in the background.
        gevent.sleep(0.1)'''