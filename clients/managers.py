from django.contrib.auth.models import BaseUserManager


class ClientManager(BaseUserManager):

    def create_user(self, email, **kwargs):
        email = self.normalize_email(email)
        user = self.model(email=email, **kwargs)
        user.save(using=self._db)
        return user

    def create_superuser(self, password=None, **kwargs):
        user = self.create_user(**kwargs)
        user.username = user.email
        user.is_superuser = True
        user.is_staff = True
        user.set_password(password)
        user.save(using=self._db)
        return user
