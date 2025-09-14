import os
import sys
import platform
import socket
import uuid

from .detectors import (
    is_colab,
    is_jupyter_notebook,
    is_running_in_docker,
    get_environment_type,
)

def get_environment_info():
    env_type = get_environment_type()

    env_info = {
        "environment": env_type,
        "os": {
            "platform": platform.system(),
            "platform_release": platform.release(),
            "platform_version": platform.version(),
            "architecture": platform.machine(),
            "hostname": socket.gethostname(),
            "ip_address": socket.gethostbyname(socket.gethostname()),
        },
        "python": {
            "version": platform.python_version(),
            "implementation": platform.python_implementation(),
            "executable": sys.executable,
        },
        "runtime": {
            "is_colab": is_colab(),
            "is_jupyter": is_jupyter_notebook(),
            "is_docker": is_running_in_docker(),
            "pid": os.getpid(),
        },
        "env_vars": {
            "USER": os.getenv("USER", ""),
            "HOME": os.getenv("HOME", ""),
            "SHELL": os.getenv("SHELL", ""),
            "PATH": os.getenv("PATH", ""),
        },
        "unique_id": str(uuid.uuid4()),
    }

    if env_type == "colab":
        env_info["colab"] = {
            "mounted_drive": os.path.exists("/content/drive"),
            "notebook_env": "Google Colab",
        }

    return env_info
