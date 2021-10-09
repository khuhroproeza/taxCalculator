import os

from dotenv import load_dotenv

load_dotenv()


def getenv(var_name: str, required: bool = True):
    env_var = os.getenv(var_name)
    if (not env_var) and required:
        raise EnvironmentError(f"Environment variable {var_name} not defined")
    return env_var
