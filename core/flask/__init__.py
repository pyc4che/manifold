from flask import Flask, render_template

from os import urandom
from base64 import b64encode

_flask = Flask(
    __name__,
    static_folder='../../static',
    template_folder='../../templates'
)

_flask.secret_key = b64encode(
    urandom(256)
).decode('utf-8')


@_flask.route('/')
def index():
    return render_template(
        'index.html'
    )
