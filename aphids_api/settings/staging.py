from .local import *
import os
import dj_database_url

# Heroku stuff for database
db_from_env = dj_database_url.config(conn_max_age=500)
DATABASES['default'].update(db_from_env)

ALLOWED_HOSTS = ['salty-tor-62302.herokuapp.com']

DEBUG = False

STATIC_ROOT = 'static/'
STATIC_URL = '/static/'
