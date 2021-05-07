import uuid

from django.db import models
from django.utils.translation import ugettext_lazy as _

from model_utils.fields import AutoCreatedField, AutoLastModifiedField


class BaseModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = AutoCreatedField(_('created_at'), db_index=True)
    updated_at = AutoLastModifiedField(_('updated_at'), db_index=True)

    class Meta:
        abstract = True
