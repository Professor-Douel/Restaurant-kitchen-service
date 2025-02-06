from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ["127.0.0.1", "ep-shiny-sunset-a2l4q73f-pooler.eu-central-1.aws.neon.tech"]


# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

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