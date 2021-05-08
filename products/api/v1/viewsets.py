from django.db.utils import IntegrityError
from django.utils.translation import gettext_lazy as _

from rest_framework.exceptions import ValidationError
from rest_framework.mixins import CreateModelMixin, DestroyModelMixin, ListModelMixin
from rest_framework.viewsets import GenericViewSet

from products.models import UNIQUE_PRODUCT_BY_CLIENT, Product
from products.utils import get_product_data

from .serializers import ProductSerializer


class ProductViewSet(CreateModelMixin, DestroyModelMixin, ListModelMixin, GenericViewSet):

    serializer_class = ProductSerializer
    lookup_field = 'external_id'

    def get_queryset(self):
        return Product.objects.filter(client=self.request.user)

    def perform_create(self, serializer):
        product_data = get_product_data(serializer.validated_data['external_id'])
        try:
            serializer.save(client=self.request.user, **product_data)
        except IntegrityError as e:
            errstr = str(e)
            if UNIQUE_PRODUCT_BY_CLIENT in errstr:
                raise ValidationError({'id': [_('Should be unique by client')]})
            raise
