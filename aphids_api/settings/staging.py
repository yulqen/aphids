from .local import *
import os
import dj_database_url

# Heroku stuff for database
db_from_env = dj_database_url.config(conn_max_age=500)
DATABASES['default'].update(db_from_env)

ALLOWED_HOSTS = ['salty-tor-62302.herokuapp.com']

DEBUG = False

MEDIA_ROOT = BASE_DIR / 'media'
STATIC_ROOT = BASE_DIR / 'static_root'
STATIC_URL = '/static/'


# we are removing this until we need to store additional static files
# which we probably won't.
# see https://stackoverflow.com/questions/19323513/heroku-django-oserror-no-such-file-or-directory-app-myappname-static#19323823

#STATICFILES_DIRS = (
#    BASE_DIR / 'static',
#)
