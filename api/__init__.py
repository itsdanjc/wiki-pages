from flask import Flask
from .response import Response, handle_error
from utils.utilities import str_to_bool, get_value
from utils.log import config_log

class Api(Flask):
    def __init__(self, config: dict):
        """Creates an instance of a Flask object for api endpoints."""
        super().__init__(__name__)

        #Set the config from .env
        self.config.from_mapping(config)

        #Set debug mode
        self.debug = str_to_bool(
            get_value(config, ("API_DEBUG", "GLOBAL_DEBUG"), False)
        )

        #Configure log
        config_log(self)

        #Register blueprints and defaults
        self.register_error_handler(Exception, handle_error)
        self.response_class = Response

        self.logger.info(f"{self.name.upper()} module configured")
