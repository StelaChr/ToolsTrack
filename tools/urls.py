from django.urls import path, include

from tools import views
from tools.views import ToolDetailView, ToolCreateView, ToolDeleteView

urlpatterns = [
    path('create/',ToolCreateView.as_view(),name='create-tool'),
    path('<int:pk>/',include([
        path('edit/',views.ToolUpdateView.as_view(),name='edit-tool'),
        path('details/', ToolDetailView.as_view(), name='tool-detail'),
        path('delete/', ToolDeleteView.as_view(), name='tool-delete'),
    ])),
]