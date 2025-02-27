import os
from flask import Flask
from utils.utilities import env_to_bool

def create_ui() -> Flask:
    """Creates an instance of a Flask object for ui."""
    app = Flask(__name__)

    #Set the config from .env
    app.config.from_prefixed_env("")

    #Set debug mode
    app.debug = env_to_bool(os.getenv("DEBUG", ""))
    
    return app
