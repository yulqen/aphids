import pytest

from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

pytestmark = pytest.mark.django_db


class TestPersonAPI:

    def test_my_user(self):
        me = User.objects.get(username='lemon')
        assert me.username == "lemon"


    def test_get_person_list_unauthenticated(self, client):
        response = client.get('/api/person/')
        assert response.status_code == 403


    def test_get_person_list_authenticated(self, client):
        client.login(username='lemon', password='lemonlemon')
        response = client.get('/api/person/')
        assert response.status_code == 200
        assert response.data[0]['first_name'] == 'Stanley'
        assert response.data[1]['first_name'] == 'Jim'


    def test_get_person_list_authenticated_token(self, client):
        token = Token.objects.get(user__username='lemon')
        client.login(username='lemon', password='lemonlemon')
        client.credentials(HTTP_AUTHORIZATION='Token' + token.key)
        response = client.get('/api/person/')
        assert response.status_code == 200
        assert response.data[0]['first_name'] == 'Stanley'
        assert response.data[1]['first_name'] == 'Jim'
