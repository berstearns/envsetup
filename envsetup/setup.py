from .detectors import get_environment_type
from .info import get_environment_info

def setup_env(env_dict=None):
    if env_dict is None:
        env_dict = get_environment_info()

    env_type = env_dict.get("environment", "unknown")
    print(f"\n[ENV_SETUP] Detected environment: {env_type}")

    if env_type == "colab":
        print("[ENV_SETUP] Setting up for Google Colab...")
        try:
            from google.colab import drive
            if not env_dict.get("colab", {}).get("mounted_drive", False):
                drive.mount('/content/drive', force_remount=True)
                print("[ENV_SETUP] Google Drive mounted.")
            else:
                print("[ENV_SETUP] Google Drive already mounted.")
        except Exception as e:
            print(f"[ENV_SETUP][ERROR] Failed to mount Google Drive: {e}")

    elif env_type == "jupyter":
        print("[ENV_SETUP] Setting up for Jupyter Notebook...")
        try:
            from IPython import get_ipython
            ipython = get_ipython()
            ipython.run_line_magic("matplotlib", "inline")
            print("[ENV_SETUP] Enabled %matplotlib inline.")
        except Exception as e:
            print(f"[ENV_SETUP][WARNING] Could not enable matplotlib inline: {e}")

    elif env_type == "docker":
        print("[ENV_SETUP] Running inside Docker.")
        print("  [INFO] Ensure volumes are mounted and dependencies are installed.")

    elif env_type == "script":
        print("[ENV_SETUP] Running as standalone Python script.")
        print("  [INFO] No special setup required.")

    else:
        print("[ENV_SETUP][WARNING] Unknown environment. No setup applied.")

    print(f"[ENV_SETUP] Python: {env_dict['python']['version']} on {env_dict['os']['platform']} ({env_dict['os']['architecture']})")
    print(f"[ENV_SETUP] Host: {env_dict['os']['hostname']} | PID: {env_dict['runtime']['pid']}")
    return env_dict
