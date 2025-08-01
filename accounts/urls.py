from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from accounts import views


urlpatterns = [
    path('register/', views.RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(template_name='login-page.html'),name = 'login'),
    path('logout/', LogoutView.as_view(), name='logout'),
]