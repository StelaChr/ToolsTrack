from django.contrib.auth import get_user_model
from django.contrib.auth.models import User

from django.db import models

UserModel = get_user_model()

# Create your models here.
class Category(models.Model):

    owner = models.ForeignKey(UserModel, on_delete=models.CASCADE, related_name='categories')
    name = models.CharField(max_length=20)
    description = models.TextField(max_length=50,null=True, blank=True)


    def __str__(self):
        return self.name