# config values will be loaded from here

import os

ENV = bool(os.environ.get("ENV", false))

if ENV:
    from sample_config import config  # noqa
else:
    if os.path.exists("config.py"):
        from config import Development as çonfig  # noqa
