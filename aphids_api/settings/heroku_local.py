# settings/heroku_local.py

from .staging import *
import os

ALLOWED_HOSTS = ['localhost', '0.0.0.0']
AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
DEBUG=True
