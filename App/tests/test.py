from unittest import TestCase
from django.test import Client

class ProjectTests(TestCase):

    def test_homepage(self):
        c = Client()
        response = c.get('/')
        self.assertEqual(response.status_code, 200)
