from .base import *
import socket

DEBUG = True

ALLOWED_HOSTS += ["*"]
SECRET_KEY = "hello"

if DEBUG:
    hostname, _, ips = socket.gethostbyname_ex(socket.gethostname())
    INTERNAL_IPS = [ip[: ip.rfind(".")] + ".1" for ip in ips] + [
        "127.0.0.1",
        "10.0.2.2",
        "185.204.109.200",
        "vm4700612.1nvme.had.wf",
    ]

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    },
}

"""THIRD-PARTY-APPS"""
INSTALLED_APPS += [
    "debug_toolbar",
    "whitenoise",
]

MIDDLEWARE = [
    "debug_toolbar.middleware.DebugToolbarMiddleware",
    "django.middleware.common.CommonMiddleware",
] + MIDDLEWARE

CELERY_BROKER_URL = 'memory://' 
