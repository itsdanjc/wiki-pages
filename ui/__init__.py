from flask import Flask
from utils.utilities import str_to_bool, get_value
from utils.log import config_log

class Ui(Flask):
    def __init__(self, config: dict):
        """Creates an instance of a Flask object for UI."""
        super().__init__(__name__)

        # Set the config from .conf
        self.config.from_mapping(config)

        # Set debug mode
        self.debug = str_to_bool(
            get_value(config, ("UI_DEBUG", "GLOBAL_DEBUG"), False)
        )

        # Configure log
        config_log(self)
        self.logger.info(f"{self.name.upper()} module configured")
