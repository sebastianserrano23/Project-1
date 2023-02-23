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
