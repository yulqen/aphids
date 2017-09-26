import json

from django.test import TestCase
from django.urls import reverse

from passes.models import PassType


class DjangoRestFrameworkTests(TestCase):

    def setUp(self):
        PassType.objects.get_or_create(pass_type='The Gold Standard!')
        PassType.objects.get_or_create(pass_type='The Silver Standard!')

        self.create_read_url = reverse('pass-type-list')
        self.read_update_delete_url = reverse('pass-type-detail', args=[1])


    def test_list(self):
        response = self.client.get(self.create_read_url)

        # Are both types in content?
        self.assertContains(response, 'The Gold Standard!')
        self.assertContains(response, 'The Silver Standard!')

#    def test_detail(self):
#        response = self.client.get(self.read_update_delete_url)
#        data = json.loads(response.content)
#        content = {'id': 1, 'pass_type': 'The Gold Standard!'}
#        self.assertEquals(data, content)
