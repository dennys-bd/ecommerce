import factory
from factory import Faker, django

from clients.tests.factories import ClientFactory
from products.models import Product


class ProductFactory(django.DjangoModelFactory):
    class Meta:
        model = Product

    external_id = Faker('uuid4')
    client = factory.SubFactory(ClientFactory)
    title = Faker('sentence')
    image = Faker('image_url')
    price = Faker('pydecimal', left_digits=4, right_digits=2)
    score = Faker('pyfloat')
