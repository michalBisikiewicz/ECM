from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse

from store.models import Category, Product

# Create your tests here.


class TestCategoriesModel(TestCase):

    def setUp(self):
        self.data1 = Category.objects.create(name='DVD', slug='DVD')

    def test_category_model_entry(self):
        """
        Test Category model data insertion/types/field attributes
        """
        data = self.data1
        self.assertTrue(isinstance(data, Category))
        self.assertEqual(str(data), 'DVD')

    def test_category_url(self):
        """
        Test category model slug and URL reverse
        """
        data = self.data1
        response = self.client.post(
            reverse('store:category_list', args=[data.slug]))
        self.assertEqual(response.status_code, 200)

    def test_category_model_name(self):
        """
        Test Category model default name
        """
        data = self.data1
        self.assertEqual(str(data), 'DVD')


class TestProductsModel(TestCase):
    def setUp(self):
        Category.objects.create(name='DVD', slug='DVD')
        User.objects.create(username='admin')
        self.data1 = Product.objects.create(category_id=1, title='Orange', created_by_id=1, slug='Orange',
                                            price='5.00', image='orange')

    def test_products_model_entry(self):
        """
        Test Products model data insertion/types/field attributes
        """
        data = self.data1
        self.assertTrue(isinstance(data, Product))
        self.assertEqual(str(data), 'Orange')

    def test_products_url(self):
        """
        Test product model slug and URL reverse
        """
        data = self.data1
        url = reverse('store:product_detail', args=[data.slug])
        self.assertEqual(url, '/Orange')
        response = self.client.post(
            reverse('store:product_detail', args=[data.slug]))
        self.assertEqual(response.status_code, 200)

    def test_products_custom_manager_basic(self):
        """
        Test product model custom manager returns only active products
        """
        data = Product.products.all()
        self.assertEqual(data.count(), 1)
