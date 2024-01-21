import os
from dotenv import load_dotenv
load_dotenv()
MODE = (os.environ.get("MODE"),)


if MODE[0] == "DEV":
    from .dev import *
elif MODE[0] == "TEST":
    from .test import *
elif MODE[0] == "PROD":
    from .prod import *
else:
    MODE = list(MODE)
    MODE[0] = "LOC"
    from .local import *