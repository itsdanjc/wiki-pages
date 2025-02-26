from flask import Flask

def create_ui() -> Flask:
    """Creates an instance of a Flask object for ui."""
    app = Flask(__name__)
    app.config.from_prefixed_env("")
    return app
