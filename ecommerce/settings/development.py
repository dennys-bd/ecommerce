from .base import *  # noqa

from datetime import timedelta
from decouple import Csv, config

SECRET_KEY = config('SECRET_KEY', 'secret')

ALLOWED_HOSTS = config('ALLOWED_HOSTS', default='*', cast=Csv())

# SHELL_PLUS_IMPORTS = []
SHELL_PLUS_PRINT_SQL = True
SHELL_PLUS = 'ipython'

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(days=30)
}
