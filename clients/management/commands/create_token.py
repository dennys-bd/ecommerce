from django.core.exceptions import ObjectDoesNotExist
from django.core.management.base import BaseCommand

from rest_framework_simplejwt.tokens import RefreshToken

from clients.models import Client


class TestRefreshToken(RefreshToken):
    @classmethod
    def for_user(cls, user):
        token = RefreshToken.for_user(user)
        token['email'] = user.email
        return token


class Command(BaseCommand):
    help = 'Creates user\'s token from designated email, used only for tests'

    def add_arguments(self, parser):
        parser.add_argument('email', nargs=1)

    def handle(self, *args, email=None, **options):  # noqa
        try:
            user = Client.objects.get(email=email[0])
        except ObjectDoesNotExist:
            user = Client(email=email[0])
        refresh = TestRefreshToken.for_user(user)
        return str(refresh.access_token)
