import pytest

from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from rest_framework.test import APIClient

pytestmark = pytest.mark.django_db


def test_my_user():
    me = User.objects.get(username='lemon')
    assert me.username == "lemon"

