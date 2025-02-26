from flask import Flask

def create_api() -> Flask:
    """Creates an instance of a Flask object for api endpoints."""
    app = Flask(__name__)
    app.config.from_prefixed_env("")
    return app
