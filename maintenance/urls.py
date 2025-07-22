from django.urls import path, include

from maintenance import views
from maintenance.views import ToolMaintenanceCreateView

urlpatterns = [
    path('<int:pk>/', include([
        path('create/',ToolMaintenanceCreateView.as_view(), name='maintenance-create'),
        path('records/',views.maintenance_records_view, name='maintenance-records' ),
    ])),
]