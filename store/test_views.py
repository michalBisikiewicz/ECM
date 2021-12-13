from importlib import import_module
from unittest import skip

from django.conf import settings
from django.http import HttpRequest
from django.test import Client, TestCase
from django.urls import reverse

from store.models import Category, Product, User
from store.views import product_all


class TestViewResponses(TestCase):

    def setUp(self):
        self.c = Client()
        Category.objects.create(name='DVD', slug='DVD')
        User.objects.create(username='admin')
        Product.objects.create(category_id=1, title='Orange', created_by_id=1, slug='Orange',
                               price='5.00', image='orange')

    def test_url_allowed_hosts(self):
        """
        Test allowed hosts
        """
        response = self.c.get('/', HTTP_HOST='noaddress.com')
        self.assertEqual(response.status_code, 400)
        response = self.c.get('/', HTTP_HOST='mydomain.com')
        self.assertEqual(response.status_code, 200)

    def test_homepage_url(self):
        """
        Test homepage response status
        """
        response = self.c.get('/')
        self.assertEqual(response.status_code, 200)

    def test_product_detail_url(self):
        """
        Test items response status
        """
        response = self.c.get(reverse('store:product_detail', args=['Orange']))
        self.assertEqual(response.status_code, 200)

    def test_category_detail_url(self):
        """
        Test category response status
        """
        response = self.c.get(reverse('store:category_list', args=['DVD']))
        self.assertEqual(response.status_code, 200)

    def test_homepage_html(self):
        """
        Example: code validation, search HTML for text
        """
        request = HttpRequest()
        engine = import_module(settings.SESSION_ENGINE)
        request.session = engine.SessionStore()
        response = product_all(request)
        html = response.content.decode('utf8')
        self.assertIn('<title>PRIMO</title>', html)
        self.assertTrue(html.startswith('\n<!DOCTYPE html>\n'))
        self.assertEqual(response.status_code, 200)
