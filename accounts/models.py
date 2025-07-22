from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import UserManager, PermissionsMixin
from django.db import models

from accounts.managers import AppUserManager


# Create your models here.
class AppUser(AbstractBaseUser, PermissionsMixin):
    USERNAME_FIELD = 'email'


    email = models.EmailField(
        unique=True
    )

    is_active = models.BooleanField(
        default=True
    )

    is_staff = models.BooleanField(
        default=False
    )

    objects = AppUserManager()





