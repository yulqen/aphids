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


@pytest.fixture(scope='session')
def client():
    """Overriding pytest-django client with DRF one."""

    from rest_framework.test import APIClient

    return APIClient()
