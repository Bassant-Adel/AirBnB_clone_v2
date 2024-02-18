#!/usr/bin/python3
"""
Flask web
"""
from flask import Flask, render_template
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
    text
    """
    return f"C {escape(text.replace('_', ' '))}"


@app.route("/python/", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python_text(text="is cool"):
    """
    PYTHON
    """
    return f"Python {escape(text.replace('_', ' '))}"


@app.route("/number/<int:n>", strict_slashes=False)
def is_a_number(n):
    """
    is a number
    """
    return f"{escape(n)} is a number"


@app.route("/number_template/<int:n>", strict_slashes=False)
def number_template(n):
    """
    page
    """
    return render_template("5-number.html", number=n)


@app.route("/number_odd_or_even/<int:n>", strict_slashes=False)
def number_odd_or_even(n):
    """
    even || odd
    """
    return render_template("6-number_odd_or_even.html", number=n)


if __name__ == '__main__':
    """
    Listening
    """
    app.run(host='0.0.0.0', port=5000)
