from unittest.mock import patch

from django.conf import settings
from django.test import TestCase

import factory
from faker import Faker
from rest_framework.exceptions import ValidationError

from common.tests_helper import Bunch
from products.utils import get_product_data

from .factories import ProductFactory


class UtilsTest(TestCase):
    @patch('products.utils.requests.get')
    def test_get_product_data(self, mocked_get):
        uuid = Faker().uuid4()
        mocked_product_data = factory.build(dict, FACTORY_CLASS=ProductFactory, client=None)
        mocked_get.side_effect = lambda x: Bunch({'ok': True, 'json': lambda: mocked_product_data})

        product_data = get_product_data(uuid)

        del mocked_product_data['external_id']
        del mocked_product_data['client']

        self.assertEqual(mocked_product_data, product_data)
        mocked_get.assert_called_once_with(f'{settings.PRODUCT_API}{uuid}/')

    @patch('products.utils.requests.get')
    def test_get_product_data_fail(self, mocked_get):
        mocked_get.side_effect = lambda x: Bunch({'ok': False})

        with self.assertRaises(ValidationError):
            get_product_data(Faker().uuid4())
