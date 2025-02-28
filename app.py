import os
from api import create_api
from ui import create_ui
from dotenv import load_dotenv
from werkzeug.middleware.dispatcher import DispatcherMiddleware
from werkzeug.serving import run_simple
from utils.utilities import env_to_bool

def create_app() -> DispatcherMiddleware:
    """Creates an instance of DispatcherMiddleware, combining the api and ui."""
    load_dotenv(override=True)


    ui_app = create_ui()
    api_app = create_api()

    return DispatcherMiddleware(ui_app, {
        '/api': api_app
    })


if __name__ == '__main__':
    app = create_app()

    run_simple(
        os.getenv("HOSTNAME", "localhost"),
        int(os.getenv("PORT", 5000)),
        app,
        use_reloader = False,
        use_debugger = env_to_bool(os.getenv("DEBUG", True)),
    )
