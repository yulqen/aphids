import pytest

from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from rest_framework import status

pytestmark = pytest.mark.django_db


class TestPassAPI:
    def test_get_pass_detail_authenticated(self, client):
        client.login(username='lemon', password='lemonlemon')
        response = client.get('/api/pass/1/')
        assert response.status_code == 200
        assert response.data['application_succeeded'] is True


    def test_get_pass_list_authenticated(self, client):
        client.login(username='lemon', password='lemonlemon')
        response = client.get('/api/pass/')
        assert response.status_code == 200
        assert response.data[0]['holder_staff_number'] == 'STAFFNO001'


    def test_get_pass_detail_unauth(self, client):
        response = client.get('/api/pass/1/')
        assert response.status_code == 403

    def test_get_pass_list_unauth(self, client):
        response = client.get('/api/pass/')
        assert response.status_code == 403


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


    def test_get_person_detail_unauth(self, client):
        response = client.get('/api/person/1/')
        assert response.status_code == 403


    def test_get_person_detail_auth(self, client):
        token = Token.objects.get(user__username='lemon')
        client.login(username='lemon', password='lemonlemon')
        client.credentials(HTTP_AUTHORIZATION='Token' + token.key)
        response = client.get('/api/person/2/')
        assert response.status_code == 200
        assert response.data['first_name'] == 'Jim'

    def test_post_person_auth(self, client, person_test_dict):
        token = Token.objects.get(user__username='lemon')
        client.login(username='lemon', password='lemonlemon')
        client.credentials(HTTP_AUTHORIZATION='Token' + token.key)
        response = client.post('/api/person/', data=person_test_dict, format='json')
        assert response.status_code == status.HTTP_201_CREATED




