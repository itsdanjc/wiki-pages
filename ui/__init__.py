import os
from flask import Flask
from utils.utilities import env_to_bool
from utils.log import config_log

def create_ui() -> Flask:
    """Creates an instance of a Flask object for ui."""
    app = Flask(__name__)

    #Set the config from .env
    app.config.from_prefixed_env("")

    #Set debug mode
    app.debug = env_to_bool(os.getenv("DEBUG", ""))
    
    #Configure log
    log = config_log(app)

    app.logger.info(f"{app.name.upper()} module configured")
    app.logger.info(f"Log at {log}")
    return app
