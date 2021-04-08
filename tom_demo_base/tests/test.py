from django.contrib.auth.models import User
from django.test import TestCase


class TestTrivialTest(TestCase):
    def setUp(self) -> None:
        # create a user for the tests
        user = User.objects.create(username='test')
        self.client.force_login(user)

    def test_index_status_code(self):
        response = self.client.get('/')
        self.assertEqual(200, response.status_code)
