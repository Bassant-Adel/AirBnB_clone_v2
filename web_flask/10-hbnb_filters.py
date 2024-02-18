#!/usr/bin/python3
"""
Flask web
"""
from flask import Flask, render_template
from models import storage
from models.state import State
from models.amenity import Amenity

app = Flask(__name__)


@app.route('/hbnb_filters', strict_slashes=False)
def hbnb_filters(id=None):
    """
    State page
    """
    slist = sorted(storage.all(
        State).values(), key=lambda x: x.name)
    for s in slist:
        s.cities.sort(key=lambda x: x.name)

    amenities_list = sorted(storage.all(
        Amenity).values(), key=lambda x: x.name)
    return render_template("10-hbnb_filters.html", sorted_states_list=slist,
                           amenities_list=amenities_list)


@app.teardown_appcontext
def terminate(exc):
    """
    termin
    """
    storage.close()


if __name__ == '__main__':
    """
    Listening
    """
    app.run(host='0.0.0.0', port=5000)
