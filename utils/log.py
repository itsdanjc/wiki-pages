import os, tempfile, logging
from flask import Flask
from datetime import datetime, timezone
from logging.config import dictConfig

logs_configured = {}
LOG_PATH = os.path.normpath(
    os.getenv("TEMP_FILE_PATH", f"{tempfile.gettempdir()}/wikipages")
)

def config_log(app: Flask) -> str:
    """Configure log handlers for the given Flask instance.
    Returns path to log file"""
    
    if app.name in logs_configured:
        return logs_configured[app.name]

    timestamp_now_utc = datetime.now(tz=timezone.utc).strftime("%Y-%m-%d")
    log_file_name = f"wikipages_{app.name}_{timestamp_now_utc}.{tempfile.gettempprefix()}.log"
    log_file_path = os.path.join(LOG_PATH, log_file_name)

    # *Note*: Disables all logging from Werkzeug (which logs HTTP requests).
    # to fix issue with ANSI characters in file.
    # As it is disabled, route access logs need to be done manually,
    # except for API where it has been done via `make_response()`
    logging.getLogger('werkzeug').disabled = True

    os.makedirs(LOG_PATH, exist_ok=True)

    dictConfig({
        'version': 1,
        'formatters': {
            'default': {
                'format': f'[{app.name.upper()}] ' + '%(levelname)s: %(message)s',
            },
            'full': {
                'format': os.getenv(
                    "LOG_FORMAT", 
                    "%(asctime)s [%(threadName)s:%(thread)d, %(filename)s:%(lineno)d] %(levelname)s: %(message)s"
                )
            }
        },
        'handlers': {
            'file_handler': {
                'class': 'logging.FileHandler',
                'filename': log_file_path,
                'mode': 'a',  # append mode
                'formatter': 'full',
                'level': os.getenv("LOG_LEVEL", "WARN").upper(),
                'encoding': 'utf-8'
            },
            'wsgi': {
                'class': 'logging.StreamHandler',
                'stream': 'ext://flask.logging.wsgi_errors_stream',
                'level': 'DEBUG',
                'formatter': 'default',
            },
        },
        'root': {
            'handlers': ['wsgi', 'file_handler']
        }
    })

    logs_configured[app.name] = log_file_path
    return log_file_path