from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from django.db import models
from django.utils import timezone

from category.models import Category

UserModel = get_user_model()

class Tool(models.Model):



    owner = models.ForeignKey(UserModel, on_delete=models.CASCADE, related_name="tools")
    category = models.ForeignKey('category.Category', on_delete=models.CASCADE, related_name='tools')
    name = models.CharField(max_length=20)
    brand_name = models.CharField(max_length=20, null=True, blank=True)
    photo = models.ImageField(null=True, blank=True, upload_to='files')
    inventory_number = models.CharField(max_length=20)
    is_borrowed = models.BooleanField(default=False)
    room = models.CharField(max_length=20, null=True, blank=True)
    section_number = models.CharField(max_length=20)


    def __str__(self):
        return f"{self.name} ({self.category})"


class Borrow(models.Model):
    tool = models.ForeignKey(Tool, on_delete=models.CASCADE, related_name='borrows')
    borrower_name = models.CharField(max_length=100)
    borrower_contact = models.CharField(max_length=100, blank=True)
    borrowed_at = models.DateTimeField(default=timezone.now)
    returned_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.tool.name} borrowed by {self.borrower_name}"