import os
from pathlib import Path

try:
    from dotenv import load_dotenv
except ImportError:
    load_dotenv = None


def load_environment_variables(dotenv_path: str = None, override: bool = True) -> dict:
    """
    Load environment variables from a .env file (if available) and merge with os.environ.

    Args:
        dotenv_path (str, optional): Path to .env file. Defaults to ".env" in cwd.
        override (bool): Whether to override existing environment variables.

    Returns:
        dict: Dictionary of environment variables (merged).
    """
    env_vars = dict(os.environ)  # start with system environment

    if load_dotenv is None:
        print("[ENV_SETUP][WARNING] python-dotenv not installed. Skipping .env loading.")
        return env_vars

    if dotenv_path is None:
        dotenv_path = Path(".env")

    if Path(dotenv_path).exists():
        load_dotenv(dotenv_path, override=override)
        env_vars.update({k: v for k, v in os.environ.items()})
        print(f"[ENV_SETUP] Loaded environment variables from {dotenv_path}")
    else:
        print(f"[ENV_SETUP][INFO] No .env file found at {dotenv_path}, skipping.")

    return env_vars

