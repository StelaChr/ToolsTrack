from django.db import models
from tools.models import Tool

# Create your models here.
class ToolMaintenance(models.Model):
    tool = models.ForeignKey('tools.Tool', on_delete=models.CASCADE, related_name='maintenance_records')
    date = models.DateField(auto_now_add=True)
    maintenance_type = models.CharField(max_length=20)  # e.g. 'Sharpening', 'Battery Replacement'
    performed_by = models.CharField(max_length=20, blank=True, null=True)  # e.g. 'Self', 'Repair Shop'
    cost = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True)
    notes = models.TextField(blank=True, null=True, max_length=100)

    class Meta:
        ordering = ['-date']

    def __str__(self):
        return f"{self.tool.name} - {self.maintenance_type} on {self.date}"