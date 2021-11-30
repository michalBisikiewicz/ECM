from django.contrib.auth.models import User
from django.test import TestCase

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
