from django.urls import path

from category import views

urlpatterns = [
    path('create', views.create_category, name='create-category'),
path('<int:category_id>/', views.category_tools_view, name='category-tools'),
]