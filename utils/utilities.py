from configparser import ConfigParser
from platformdirs import site_config_dir
import os, typing

global CONFIG_PATH
CONFIG_PATH = os.path.join(site_config_dir("wikipages", ensure_exists=True), "wikipages.conf")

def get_config() -> dict:

    if not os.path.exists(CONFIG_PATH):
        print(f"Config not found at {CONFIG_PATH}. Run the installer (install.py) to configure")
        return {}

    config_parser = ConfigParser()
    config_parser.read(CONFIG_PATH)

    config_object = {}

    for section in config_parser.sections():
        for item, value in config_parser.items(section):
            config_object[f'{section}_{item}'.upper()] = value

    return config_object

def str_to_bool(str: t.Any) -> bool:
    return f"{str}".lower() in {"1", "yes", "true"}

def get_value(
    config: Config | t.Mapping[t.Any, t.Any],
    keys: t.Iterable[t.Any],
    default: t.Any | None = None
) -> str:
    """Retrieve the first available value from the config using a list of keys."""
    for key in keys:
        value: str = config.get(key)
        if value: return value
    return default