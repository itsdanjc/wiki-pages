import os
from flask import Flask
from .response import Response, handle_error
from utils.utilities import env_to_bool
from utils.log import config_log

def create_api() -> Flask:
    """Creates an instance of a Flask object for api endpoints."""
    app = Flask(__name__)

    #Set the config from .env
    app.config.from_prefixed_env("")

    #Set debug mode
    app.debug = env_to_bool(os.getenv("DEBUG", ""))

    #Configure log
    log = config_log(app)

    #Register blueprints and defaults
    app.register_error_handler(Exception, handle_error)
    app.response_class = Response

    app.logger.info(f"{app.name.upper()} module configured")
    app.logger.info(f"Log at {log}")
    return app
