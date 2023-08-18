#!/usr/bin/python3
"""script that starts a Flask web application"""

from flask import Flask, render_template
from markupsafe import escape
from models import storage
from models.state import State

app = Flask(__name__)


@app.route("/states_list", strict_slashes=False)
def states_list():
    """html page with a list of all state objects sorted az"""
    states = storage.all(State)
    sorted_states = sorted(states, key=lambda state: state.name)
    return render_template("7-states_list.html", states=sorted_states)


@app.teardown_appcontext
def teardown_session(exception):
    """remove the current SQLAlchemy Session"""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
