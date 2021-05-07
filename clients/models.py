# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from common.models import BaseModel


class Client(BaseModel):
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
