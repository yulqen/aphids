from .local import *
import os
import dj_database_url

# Heroku stuff for database
db_from_env = dj_database_url.config(conn_max_age=500)
DATABASES['default'].update(db_from_env)

ALLOWED_HOSTS = ['salty-tor-62302.herokuapp.com']

DEBUG = False

# not using for now
#MEDIA_ROOT = BASE_DIR / 'media'
STATIC_ROOT = BASE_DIR / 'static_root'


# we are removing this until we need to store additional static files
# which we probably won't.
# see https://stackoverflow.com/questions/19323513/heroku-django-oserror-no-such-file-or-directory-app-myappname-static#19323823

#STATICFILES_DIRS = (
#    BASE_DIR / 'static',
#)

# AWS settings
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
STATIC_FILES_STORAGES = 'storages.backends.s3boto3.s3Boto3Storage'
AWS_STORAGE_BUCKET_NAME = 'aphids-test'

STATIC_URL = "http://" + AWS_STORAGE_BUCKET_NAME + ".s3.amazonaws.com/"
