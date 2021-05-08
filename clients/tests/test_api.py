from http import HTTPStatus
from io import StringIO

from django.core.exceptions import ObjectDoesNotExist
from django.core.management import call_command
from django.test import TestCase
from django.urls import reverse

from faker import Faker
from rest_framework.test import APIClient

from clients.models import Client

from .factories import ClientFactory


CLIENT_ENDPOINT = reverse('client-detail')


class ApiTest(TestCase):

    def setUp(self):
        self.client = APIClient()
        self.user = ClientFactory()
        self.client.force_authenticate(self.user)
        self.fake = Faker()

    def test_retrieve(self):
        res = self.client.get(CLIENT_ENDPOINT)
        body = res.json()

        self.assertEqual(res.status_code, HTTPStatus.OK)
        self.assertEqual(body['email'], self.user.email)
        self.assertEqual(body['name'], self.user.name)

    def test_update(self):

        old_name = self.user.name
        old_email = self.user.email

        payload = {
            'name': self.fake.name(),
            'email': self.fake.email()
        }

        res = self.client.put(CLIENT_ENDPOINT, payload)
        body = res.json()

        self.assertEqual(res.status_code, HTTPStatus.OK)
        self.assertEqual(body['email'], payload['email'])
        self.assertEqual(body['name'], payload['name'])
        self.assertNotEqual(body['email'], old_email)
        self.assertNotEqual(body['name'], old_name)

    def test_delete(self):

        res = self.client.delete(CLIENT_ENDPOINT)

        self.assertEqual(res.status_code, HTTPStatus.NO_CONTENT)

        with self.assertRaises(ObjectDoesNotExist):
            Client.objects.get(id=self.user.id)


class ApiAuthorizationTest(TestCase):

    def setUp(self):
        self.client = APIClient()
        self.user = ClientFactory()
        self.fake = Faker()

    def test_retrieve(self):
        res = self.client.get(CLIENT_ENDPOINT)

        self.assertEqual(res.status_code, HTTPStatus.UNAUTHORIZED)

    def test_create_new_user(self):
        email = self.fake.email()
        token = call_command('create_token', email, stdout=StringIO())
        payload = {'name': self.fake.name()}

        self.assertEqual(Client.objects.count(), 1)

        res = self.client.patch(CLIENT_ENDPOINT, payload, HTTP_AUTHORIZATION=f'Bearer {token}')
        body = res.json()

        self.assertEqual(res.status_code, HTTPStatus.OK)
        self.assertEqual(email, body['email'])
        self.assertEqual(payload['name'], body['name'])
        self.assertEqual(Client.objects.count(), 2)
