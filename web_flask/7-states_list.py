#!/usr/bin/python3
"""
Flask web
"""
from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def states_list():
    """
    States
    """
    sortedlist = sorted(storage.all(
        State).values(), key=lambda x: x.name)
    return render_template("7-states_list.html", sorted_states_list=sortedlist)


@app.teardown_appcontext
def terminate(exc):
    """
    CLOSE
    """
    storage.close()


if __name__ == '__main__':
    """
    Listening
    """
    app.run(host='0.0.0.0', port=5000)
