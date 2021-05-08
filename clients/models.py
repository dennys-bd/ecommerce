# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils.translation import ugettext_lazy as _

from common.models import BaseModel

from .managers import ClientManager


class Client(AbstractBaseUser, PermissionsMixin, BaseModel):
    email = models.EmailField(_('email'), max_length=255, unique=True)
    name = models.CharField(_('name'), max_length=255)
    password = models.CharField(max_length=128, blank=True, null=True)

    USERNAME_FIELD = 'email'

    is_staff = models.BooleanField(
        default=False,
        help_text=_('Designates whether the user can log into this admin '
                    'site.'))
    is_active = models.BooleanField(
        default=True,
        help_text=_('Designates whether this user should be treated as '
                    'active. Unselect this instead of deleting accounts.'))

    objects = ClientManager()
