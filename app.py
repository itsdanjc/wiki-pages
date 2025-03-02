import os
from api import Api
from ui import Ui
from flask import Config
from werkzeug.middleware.dispatcher import DispatcherMiddleware
from werkzeug.serving import run_simple
from utils.utilities import get_config, str_to_bool

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
        config.get("GLOBAL_HOSTNAME", "localhost"),
        int(os.getenv("GLOBAL_PORT", 5000)),
        app,
        use_reloader = str_to_bool(config.get("GLOBAL_RELOADER", "1")),
        use_debugger = str_to_bool(config.get("GLOBAL_DEBUG", "1")),
        threaded=True
    )
