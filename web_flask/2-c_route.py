#!/usr/bin/python3
"""python module that starts a web flask app"""
from flask import Flask, escape
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """returns hello HBNB"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """returns HBNB path"""
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def some_text():
    """returns sometext passed in"""
    text = escape(text.replace('_', ' '))
    return 'C {}'.format(text)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
