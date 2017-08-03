from .base import *

DEBUG = True

# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

ALLOWED_HOSTS = [
    'localhost',
    '127.0.0.1',
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'aphids_api',
        'USER': 'lemon',
        'PASSWORD': 'lemon',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
