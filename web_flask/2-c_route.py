#!/usr/bin/python3
"""
Flask web
"""
from flask import Flask
from markupsafe import escape
app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hbnb():
    """
    Hell
    """
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """
    hbnb
    """
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c_text(text):
    """
    C Text
    """
    return f"C {escape(text.replace('_', ' '))}"


if __name__ == '__main__':
    """
    Listening
    """
    app.run(host='0.0.0.0', port=5000)
