from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

class UserManager(AbstractBaseUser):
    def create_user(self, username, email, password = None):
        if not email:
            raise ValueError("Not a valid email address")

        user = self.model(
            email = self.normalize_email(email),
            username = username,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password=None):
        user = self.create_user(
            email = self.normalize_email(email),
            password = password,
            username = username,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user

