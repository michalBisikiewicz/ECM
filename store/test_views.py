from unittest import skip
from django.test import TestCase
from django.test import Client
from django.urls import reverse
from store.models import Category, Product, User
from django.http import HttpRequest
from store.views import all_products


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
        response = self.c.get('/')
        self.assertEqual(response.status_code, 200)

    def test_product_detail_url(self):
        response = self.c.get(reverse('store:product_detail', args=['Orange']))
        self.assertEqual(response.status_code, 200)

    def test_category_detail_url(self):
        response = self.c.get(reverse('store:category_list', args=['DVD']))
        self.assertEqual(response.status_code, 200)

    def test_homepage_html(self):
        request = HttpRequest()
        response = all_products(request)
        html = response.content.decode('utf8')
        print(html)
        self.assertIn('<title>Home</title>', html)
        self.assertTrue(html.startswith('\n<!DOCTYPE html>\n'))
        self.assertEqual(response.status_code, 200)
