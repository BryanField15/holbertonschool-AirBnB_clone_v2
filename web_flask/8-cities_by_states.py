#!/usr/bin/python3
"""A script that starts a Flask web application"""
from flask import Flask, render_template
from markupsafe import escape
from models import storage
from models.state import State
from models.city import City

app = Flask(__name__)


@app.route('/cities_by_states', strict_slashes=False)
def list_objects():
    """Displays a HTML page"""
    return render_template(
        '8-cities_by_states.html',
        states=storage.all(State),
        cities=storage.all(City))


@app.teardown_appcontext
def teardown_db(exception):
    """ remove the current SQLAlchemy Session"""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
