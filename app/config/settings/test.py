from .base import *
import socket

DEBUG = True
ALLOWED_HOSTS += ["*"]

if DEBUG:
    hostname, _, ips = socket.gethostbyname_ex(socket.gethostname())
    INTERNAL_IPS = [ip[: ip.rfind(".")] + ".1" for ip in ips] + [
        "127.0.0.1",
        "10.0.2.2",
    ]
    
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "HOST": os.environ.get("DB_HOST"),
        "NAME": os.environ.get("DB_NAME"),
        "USER": os.environ.get("DB_USER"),
        "PASSWORD": os.environ.get("DB_PASSWORD"),
    },
    "sqlite": {
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
    'whitenoise.middleware.WhiteNoiseMiddleware',
    "debug_toolbar.middleware.DebugToolbarMiddleware",
    "django.middleware.common.CommonMiddleware",
] + MIDDLEWARE

CELERY_BROKER_URL = 'redis://redis_test:6379/0'
CELERY_RESULT_BACKEND = 'redis://redis_test:6379/0'
