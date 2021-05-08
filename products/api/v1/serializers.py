from rest_framework.serializers import ModelSerializer, UUIDField

from products.models import Product


class ProductSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'title', 'image', 'price', 'score')
        read_only_fields = ('title', 'image', 'price', 'score')

    id = UUIDField(source='external_id')
    lookup_field = 'external_id'
