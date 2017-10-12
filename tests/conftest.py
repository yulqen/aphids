import pytest


@pytest.fixture(scope='session')
def django_db_setup():
    from django.conf import settings
    settings.DATABASES['default'] = {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'aphids_api',
        'USER': 'lemon',
        'PASSWORD': 'lemon',
        'HOST': 'localhost',
        'PORT': '5432',
    }
