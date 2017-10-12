import pytest

from datetime import date


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


def date_handler(obj):
    if hasattr(obj, 'isoformat'):
        return obj.isoformat()
    else:
        raise TypeError


@pytest.fixture(scope='session')
def person_test_dict():
    """No need to convert to json - the APIClient does that for you in the test."""
    person = {
        'role': 1,
        'first_name': "Shanno",
        'middle_name': "Dieter",
        'surname': "Shelsey",
        'previous_surname': "",
        'dob': date(2000, 12, 25),
        'place_of_birth': "Javid, Texas",
        'country_of_birth': "United States",
        'address': 1,
        'nationality': 'American',
        'passport_no': 'AADD2233',
        'driving_license_no': 'CDF132392AUS',
        'nat_ins': 'GH 23 23 14 D',
        'employer': 1,
        'employed_since': date(2013, 1, 12),
        'line_manager': 2,
        'telecoms': 1,
        'biometrics': 1,
        'vetting_type': 1,
        'vetting_start': date(2011, 1, 22),
        'vetting_ref': "No - not here",
        'vetting_expiry': date(2019, 1, 10),
        'vetting_terminated': False,
        'vetting_terminated_comment': ''
    }
    return person

