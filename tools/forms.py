from django import forms
from django.core.exceptions import ValidationError

from category.models import Category
from .models import Tool, Borrow

from django import forms
from .models import Tool, Category


class BaseClassToolForm(forms.ModelForm):
    class Meta:
        model = Tool
        fields = ['category', 'name', 'brand_name', 'photo', 'inventory_number', 'is_borrowed', 'room', 'section_number']


class CreateToolForm(BaseClassToolForm):


    class Meta:
        model = Tool
        fields = ['category', 'name', 'brand_name', 'photo', 'inventory_number', 'is_borrowed', 'room', 'section_number']
        widgets = {
            "category": forms.Select(attrs={'class': 'form-select', 'placeholder': 'Choose from the dropdown'}),
            "name": forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Name of the tool'}),
            "brand_name": forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Name of the tool brand'}),
            "photo": forms.ClearableFileInput(attrs={'class': 'form-control'}),
            "inventory_number": forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Number by which you track the tool'}),
            "is_borrowed": forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'room': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Room where you store the tool'}),
            'section_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Number of the drawer, shelf, container'}),
        }

        labels = {
            'category': 'Category',
            'name': 'Tool Name',
            'brand_name': 'Brand Name',
            'photo': 'Photo',
            'inventory_number': 'Inventory Number',
            'is_borrowed': 'Is Borrowed',
        }


    def __init__(self, *args, user=None, **kwargs):
        super().__init__(*args, **kwargs)
        if user and user.is_authenticated:
            self.fields['category'].queryset = Category.objects.all()  # or filter by user
        else:
            self.fields['category'].queryset = Category.objects.none()




class BorrowForm(forms.ModelForm):
    class Meta:
        model = Borrow
        fields = ['borrower_name', 'borrower_contact', 'borrowed_at', 'returned_at']
        widgets = {
            'borrower_name': forms.TextInput(attrs={'class': 'form-control', 'label': 'Borrower Name'}),
            'borrower_contact': forms.TextInput(attrs={'class': 'form-control', 'label': 'Borrower Contact', 'placeholder': 'Email, phone etc.'}),
            'borrowed_at': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date'  # this makes it a browser-native datetime picker
            }),
            'returned_at': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date'  # this makes it a browser-native datetime picker
            }),
        }

    def clean(self):
        cleaned_data = super().clean()
        borrowed_at = cleaned_data.get('borrowed_at')
        returned_at = cleaned_data.get('returned_at')
        if borrowed_at and returned_at and returned_at < borrowed_at:
            raise ValidationError("Return date cannot be before borrow date.")
        return cleaned_data


class ToolEditForm(BaseClassToolForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['photo'].widget = forms.FileInput(attrs={
            'accept': 'image/*',
            'class': 'custom-file-upload'
        })


