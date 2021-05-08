from http import HTTPStatus
from unittest.mock import patch

from django.test import TestCase
from django.urls import reverse

import factory
from faker import Faker
from rest_framework.test import APIClient

from products.models import Product

from .factories import ProductFactory


PRODUCT_ENDPOINT = reverse('product-list')


class ApiTest(TestCase):

    def get_product_data(self):
        product_data = factory.build(dict, FACTORY_CLASS=ProductFactory, client=None)
        del product_data['external_id']
        del product_data['client']
        return product_data

    def setUp(self):
        self.client = APIClient()
        self.product = ProductFactory()
        self.client.force_authenticate(self.product.client)

    def test_list(self):
        ProductFactory.create_batch(5)
        ProductFactory.create_batch(5, client=self.product.client)

        res = self.client.get(PRODUCT_ENDPOINT)
        body = res.json()

        self.assertEqual(res.status_code, HTTPStatus.OK)
        self.assertEqual(6, len(body))

    def test_delete(self):
        res = self.client.delete(f'{PRODUCT_ENDPOINT}{self.product.external_id}/')

        self.assertEqual(res.status_code, HTTPStatus.NO_CONTENT)
        self.assertEqual(0, Product.objects.count())

    @patch('products.api.v1.viewsets.get_product_data')
    def test_create(self, mocked_get_product_data):
        mocked_get_product_data.side_effect = lambda x: self.get_product_data()
        payload = {'id': Faker().uuid4()}

        res = self.client.post(PRODUCT_ENDPOINT, payload)
        body = res.json()

        self.assertEqual(HTTPStatus.CREATED, res.status_code)
        self.assertEqual(2, Product.objects.count())
        self.assertEqual(payload['id'], body['id'])

        product = Product.objects.get(external_id=payload['id'])

        self.assertEqual(self.product.client, product.client)

    @patch('products.api.v1.viewsets.get_product_data')
    def test_create_duplicated(self, mocked_get_product_data):
        mocked_get_product_data.side_effect = lambda x: self.get_product_data()
        payload = {'id': self.product.external_id}

        res = self.client.post(PRODUCT_ENDPOINT, payload)
        body = res.json()

        self.assertEqual(HTTPStatus.BAD_REQUEST, res.status_code)
        self.assertEqual(body['id'][0], 'Should be unique by client')

    def test_create_inexistent_id(self):
        payload = {'id': Faker().uuid4()}

        res = self.client.post(PRODUCT_ENDPOINT, payload)
        body = res.json()

        self.assertEqual(HTTPStatus.BAD_REQUEST, res.status_code)
        self.assertEqual(body['id'][0],
                         f'Product {payload["id"]} doesn\'t exist on the product api')
