from unittest import skip
from django.test import TestCase


@skip("demonstrating skipping")
class TestSkip(TestCase):
    def test_skip_example(self):
        """
        Demonstrating skipping a test
        """
        pass
