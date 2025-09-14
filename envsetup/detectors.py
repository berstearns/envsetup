import os

def is_colab():
    try:
        import google.colab  # noqa
        return True
    except ImportError:
        return False

def is_jupyter_notebook():
    try:
        from IPython import get_ipython
        shell = get_ipython().__class__.__name__
        return 'ZMQInteractiveShell' in shell
    except Exception:
        return False

def is_running_in_docker():
    try:
        with open('/proc/1/cgroup', 'rt') as f:
            content = f.read()
            if 'docker' in content or 'kubepods' in content:
                return True
    except FileNotFoundError:
        pass
    return os.path.exists('/.dockerenv')

def get_environment_type():
    if is_colab():
        return "colab"
    elif is_jupyter_notebook():
        return "jupyter"
    elif is_running_in_docker():
        return "docker"
    else:
        return "script"
