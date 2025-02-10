from .base import *


DEBUG = False

ALLOWED_HOSTS = ["127.0.0.1", "restaurant-kitchen-service-1-lpkh.onrender.com"]

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": os.environ['POSTGRES_DB'],
        "USER": os.environ['POSTGRES_USER'],
        "PASSWORD": os.environ['POSTGRES_PASSWORD'],
        "HOST": os.environ['POSTGRES_HOST'],
        "PORT": int(os.environ['POSTGRES_DB_PORT']),
    }
}
