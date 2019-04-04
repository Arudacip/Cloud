import os

from flask import Flask, render_template
from flask_sockets import Sockets

app = Flask(__name__)
app.debug = 'DEBUG' in os.environ
sockets = Sockets(app)

@app.route('/')
def hello():
    return render_template('index.html')


if __name__ == '__main__':
    app.debug = True
    app.run(host = 'localhost', port=5050)
