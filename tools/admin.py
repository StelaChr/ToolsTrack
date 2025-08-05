from django.contrib import admin

from accounts import models
from tools.models import Tool


# Register your models here.
@admin.register(Tool)
class ToolsAdmin(admin.ModelAdmin):
    list_display = ("owner", "category", "inventory_number","brand_name")
    list_filter = ("category__name", "is_borrowed", "brand_name")
    search_fields = ("name","category__name", "brand_name")
