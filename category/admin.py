from django.contrib import admin

from category.models import Category


# Register your models here.
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("owner", "name", "description")
    list_filter = ("name", "description")
    search_fields = ("owner", "name", "description")
