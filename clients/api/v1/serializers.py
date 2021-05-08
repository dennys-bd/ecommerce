from rest_framework.serializers import ModelSerializer

from clients.models import Client
from products.api.v1.serializers import ProductSerializer


class ClientSerializer(ModelSerializer):
    products = ProductSerializer(many=True, read_only=True)

    class Meta:
        model = Client
        fields = ('email', 'name', 'products')
