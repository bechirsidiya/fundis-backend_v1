from .base import *

DEBUG = True

ALLOWED_HOSTS = ["127.0.0.1", "localhost"]


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'fundis_db',
        'USER': 'fundis_user',
        'PASSWORD': 'strongpassword',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}