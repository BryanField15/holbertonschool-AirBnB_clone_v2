#!/usr/bin/python3
"""script that starts a Flask web application"""

from flask import Flask, render_template
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


@app.route("/number_template/", strict_slashes=False)
@app.route("/number_template/<int:n>", strict_slashes=False)
def number_template_route(n=None):
    """Variable number html template route"""
    return render_template("5-number.html", n=n)


@app.route("/number_odd_or_even/", strict_slashes=False)
@app.route("/number_odd_or_even/<int:n>", strict_slashes=False)
def number_odd_or_even_route(n=None):
    """Variable odd or even number html template route"""
    return render_template("6-number_odd_or_even.html", n=n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
