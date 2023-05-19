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


@app.route('/python/', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def show_python():
    """shows the sub_path"""
    text = escape(text.replace('_', ' '))
    return 'Python {}'.format(text)


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    """return number of times"""
    return '{} is a number'.format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def template_number():
    """displays html"""
    if isinstance(n, int):
        return render_template('5-number.html', number=n)
    else:
        return 'Invalid input'


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
