from django.db import models

from common.models import BaseModel


UNIQUE_PRODUCT_BY_CLIENT = 'unique product by client'


class Product(BaseModel):
    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['external_id', 'client'],
                                    name=UNIQUE_PRODUCT_BY_CLIENT)
        ]

    external_id = models.UUIDField()
    client = models.ForeignKey('clients.Client', related_name='products',
                               related_query_name='product', on_delete=models.CASCADE)

    title = models.CharField(max_length=255)
    image = models.URLField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    score = models.FloatField(blank=True, null=True)
