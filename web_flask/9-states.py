#!/usr/bin/python3
"""A script that starts a Flask web application"""
from flask import Flask, render_template
from markupsafe import escape
from models import storage
from models.state import State
from models.city import City

app = Flask(__name__)


@app.route('/states', strict_slashes=False)
def display_states():
    """Displays a HTML page"""
    return render_template(
        '9-states.html',
        states=storage.all(State))


@app.route('/states/<id>', strict_slashes=False)
def list_city_states(id=None):
    """html page with a list of all state objects sorted az"""
    states = storage.all(State)
    if id:
        found = False
        for state in states.values():
            if id == state.id:
                found = True
        if found is False:
            id = 'not_found'
    return render_template(
        '9-states.html',
        states=states,
        cities=storage.all(City),
        id=id, )


@app.teardown_appcontext
def teardown_db(exception):
    """ remove the current SQLAlchemy Session"""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
