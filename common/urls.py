from common import views
from django.urls import path

from common.views import HomePageView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('dashboard/', views.dashboard_view, name='dashboard'),

]