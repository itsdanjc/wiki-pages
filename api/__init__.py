from flask import Flask
from .response import Response, handle_error
from utils.utilities import env_to_bool
import os

def create_api() -> Flask:
    """Creates an instance of a Flask object for api endpoints."""
    app = Flask(__name__)

    #Set the config from .env
    app.config.from_prefixed_env("")

    #Set debug mode
    app.debug = env_to_bool(os.getenv("DEBUG", ""))

    #Register blueprints and defaults
    app.register_error_handler(Exception, handle_error)
    app.response_class = Response

    return app
