#!/usr/bin/python3
"""python module that starts a web flask app"""
from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """returns hello HBNB"""
    return 'Hello HBNB!'


if __name__ == "__main__":
    app.run(host='127.0.0.1', port=5000)
