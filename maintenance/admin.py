from django.contrib import admin
from maintenance.models import ToolMaintenance

# Register your models here.
@admin.register(ToolMaintenance)
class MaintenanceAdmin(admin.ModelAdmin):
    list_display = ("tool", "maintenance_type", "performed_by","cost")
    list_filter = ("maintenance_type", "performed_by","cost")
    search_fields = ("tool", "maintenance_type", "performed_by","cost")
    ordering = ("cost", )
    list_editable = ("cost",)