from factory import Faker, django

from clients.models import Client


class ClientFactory(django.DjangoModelFactory):
    class Meta:
        model = Client

    email = Faker('email')
    name = Faker('name')
