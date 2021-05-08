from django.contrib.auth import get_user_model

from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.exceptions import AuthenticationFailed
from rest_framework_simplejwt.settings import api_settings


class EJWTAuthentication(JWTAuthentication):

    def authenticate(self, request):
        header = self.get_header(request)

        if header is None:
            return None

        raw_token = self.get_raw_token(header)
        if raw_token is None:
            return None

        validated_token = self.get_validated_token(raw_token)

        try:
            return self.get_user(validated_token), validated_token
        except AuthenticationFailed:
            return get_user_model().objects.create(
                email=validated_token['email'], id=validated_token[api_settings.USER_ID_CLAIM]
            ), validated_token
