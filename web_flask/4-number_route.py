#!/usr/bin/python3
"""script that starts a Flask web application"""

from flask import Flask
from markupsafe import escape

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_route():
    """First route"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb_route():
    """Second route"""
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c_route(text):
    """Variable c route"""
    formatted_text = text.replace("_", " ")
    return f"C {escape(formatted_text)}"


@app.route('/python/', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python_route(text):
    """Variable python route"""
    formatted_text = text.replace("_", " ")
    return f"Python {escape(formatted_text)}"


@app.route("/number/<int:n>", strict_slashes=False)
def number_route(n):
    """Variable number route"""
    return f"{escape(n)} is a number"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
