# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils.translation import ugettext_lazy as _

from common.models import BaseModel


class Client(AbstractBaseUser, PermissionsMixin, BaseModel):
    email = models.EmailField(_('email'), max_length=255, unique=True)
    name = models.CharField(_('name'), max_length=255)
    password = models.CharField(max_length=128, blank=True, null=True)

    USERNAME_FIELD = 'email'
