import os
from api import Api
from ui import Ui
from flask import Config
from werkzeug.middleware.dispatcher import DispatcherMiddleware
from werkzeug.serving import run_simple
from utils.utilities import get_config

def create_app() -> DispatcherMiddleware:
    """Creates an instance of DispatcherMiddleware, combining the api and ui."""

    #Set config
    config = get_config()

    ui = Ui(config)
    api = Api(config)

    return DispatcherMiddleware(ui, {
        '/api': api
    })


if __name__ == '__main__':
    app = create_app()
    config = get_config()

    run_simple(
        os.getenv("HOSTNAME", "localhost"),
        int(os.getenv("PORT", 5000)),
        app,
        use_reloader = config.get("USE_RELOADER", "1").lower() in {"1", "yes", "true"},
        use_debugger = config.get("USE_DEBUG", "1").lower() in {"1", "yes", "true"},
    )
