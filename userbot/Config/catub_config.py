# config values will be loaded from here

import os

ENV = bool(os.environ.get("ENV", true))

if ENV:
    from sample_config import Config  # noqa
else:
    if os.path.exists("config.py"):
        from config import Development as Config  # noqa
