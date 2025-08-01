from django import forms

from maintenance.models import ToolMaintenance


class ToolMaintenanceForm(forms.ModelForm):
    class Meta:
        model = ToolMaintenance
        fields = ['maintenance_type', 'performed_by', 'cost', 'notes']
        widgets = {
            'maintenance_type': forms.TextInput(attrs={'class': 'form-control', 'placeholder': ' Example: regular cleaning, repairs, replacements of worn parts etc.'}),
            'performed_by': forms.TextInput(attrs={'class': 'form-control', 'placeholder': ' Example: Individual or team you hire'}),
            'cost': forms.NumberInput(attrs={'class': 'form-control'}),
            'notes': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }