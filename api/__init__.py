from flask import Flask
from .response import Response

def create_api() -> Flask:
    """Creates an instance of a Flask object for api endpoints."""
    app = Flask(__name__)
    app.config.from_prefixed_env("")
    app.response_class = Response
    return app
