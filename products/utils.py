from django.conf import settings
from django.utils.translation import gettext_lazy as _

import requests
from rest_framework.exceptions import ValidationError


wanted_keys = ('title', 'image', 'price', 'score')


def get_product_data(product_id):
    res = requests.get(f'{settings.PRODUCT_API}{product_id}/')

    if not res.ok:
        raise ValidationError(
            {'id': [_(f'Product {product_id} doesn\'t exist on the product api')]})

    return {key: value for (key, value) in res.json().items() if key in wanted_keys}
