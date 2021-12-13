from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse

from store.models import Category, Product


class TestBasketView(TestCase):

    def setUp(self):
        Category.objects.create(name='DVD', slug='DVD')
        User.objects.create(username='admin')
        Product.objects.create(category_id=1, title='Orange', created_by_id=1, slug='Orange',
                               price='5.00', image='orange')
        Product.objects.create(category_id=1, title='orange_2', created_by_id=1, slug='orange_2',
                               price='1.00', image='default')
        Product.objects.create(category_id=1, title='orange_3', created_by_id=1, slug='orange_3',
                               price='1.00', image='default')
        self.client.post(
            reverse('basket:basket_add'), {"productid": 1, "productqty": 1, "action": "post"}, xhr=True)
        self.client.post(
            reverse('basket:basket_add'), {"productid": 2, "productqty": 2, "action": "post"}, xhr=True)

    def test_basket_url(self):
        """
        Test homepage response status
        """
        response = self.client.get(reverse('basket:basket_summary'))
        self.assertEqual(response.status_code, 200)

    def test_basket_add(self):
        """
        Testing adding items to the basket
        """
        response = self.client.post(
            reverse('basket:basket_add'), {"productid": 3, "productqty": 1, "action": "post"}, xhr=True)
        self.assertEqual(response.json(), {'qty': 4})
        response = self.client.post(
            reverse('basket:basket_add'), {"productid": 2, "productqty": 1, "action": "post"}, xhr=True)
        self.assertEqual(response.json(), {'qty': 5})

    def test_basket_delete(self):
        """
        Test deleting items from the basket
        """
        response = self.client.post(
            reverse('basket:basket_delete'), {"productid": 2, "action": "post"}, xhr=True)
        self.assertEqual(response.json(), {'qty': 1, "subtotal": '5.00'})

    def test_basket_update(self):
        """
        Test updating items from the basket
        """
        response = self.client.post(
            reverse('basket:basket_update'), {"productid": 2, "productqty": 1, "action": "post"}, xhr=True)
        self.assertEqual(response.json(), {'qty': 2, "subtotal": '6.00'})
