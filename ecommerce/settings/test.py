import logging

from .development import *  # noqa


PASSWORD_HASHERS = [
    'django.contrib.auth.hashers.MD5PasswordHasher',
]

logging.disable(logging.CRITICAL)
