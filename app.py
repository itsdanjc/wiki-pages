from api import create_api
from ui import create_ui
from dotenv import load_dotenv
from werkzeug.middleware.dispatcher import DispatcherMiddleware
from werkzeug.serving import run_simple
import os

def create_app() -> DispatcherMiddleware:
    """Creates an instance of DispatcherMiddleware, combining the api and ui."""
    if not os.environ.get("ENV_LOADED"):  
        load_dotenv()
        os.environ["ENV_LOADED"] = "1"


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
        use_reloader=True,
        use_debugger=True
    )
