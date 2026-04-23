from .base import *
import os

DEBUG = False

ALLOWED_HOSTS = [os.environ.get("DOMAIN")]

SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True