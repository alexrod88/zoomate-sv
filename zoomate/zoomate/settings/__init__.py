from .base import *
import os

env_name = os.getenv("API_ENV", "dev")

if env_name == "prod":
    from .prod import *
elif env_name == "stage":
    from .stage import *
else:
    from .dev import *
