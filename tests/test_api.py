import json

from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from rest_framework.test import force_authenticate
from rest_framework.test import APIRequestFactory

from passes.models import PassType
from passes.views import PassTypeList


class DjangoRestFrameworkTests(TestCase):

    def setUp(self):
        self.factory = APIRequestFactory()
        User.objects.get_or_create(username='test_lemon', password='test')
        for user in User.objects.all():
            Token.objects.get_or_create(user=user)
        PassType.objects.get_or_create(pass_type='The Gold Standard!')
        PassType.objects.get_or_create(pass_type='The Silver Standard!')
        self.user = User.objects.get(id=1)
        self.view = PassTypeList.as_view()

        self.create_read_url = reverse('pass-type-list')
        self.read_update_delete_url = reverse('pass-type-detail', args=[1])


    def test_list(self):
        request = self.factory.get(self.create_read_url)
        force_authenticate(request, user=self.user)
        response = self.view(request)

        # Are both types in content?
        self.assertContains(response, 'The Gold Standard!')
        self.assertContains(response, 'The Silver Standard!')

#    def test_detail(self):
#        response = self.client.get(self.read_update_delete_url)
#        data = json.loads(response.content)
#        content = {'id': 1, 'pass_type': 'The Gold Standard!'}
#        self.assertEquals(data, content)
