def env_to_bool(env: str) -> bool:
    return str(env).lower() in ("1", "true", "yes")