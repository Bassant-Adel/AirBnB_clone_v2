#!/usr/bin/python3
"""
Flask web
"""
from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_route():
    """
    Hell
    """
    return "Hello HBNB!"


if __name__ == '__main__':
    """
    Listening
    """
    app.run(host='0.0.0.0', port=5000)
