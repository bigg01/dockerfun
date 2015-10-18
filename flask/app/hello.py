#!flask/bin/python
from flask import render_template
from flask import Flask
import os
app = Flask(__name__)

env = os.environ

@app.route('/')
def hello():
    return render_template('hello.html', env=env)

if __name__ == '__main__':
    app.run(host='0.0.0.0')
