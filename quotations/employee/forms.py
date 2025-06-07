# forms.py
from django import forms
from .models import product_need

class productNeedForm(forms.ModelForm):
    class Meta:
        model = product_need
        fields = '__all__'
        widgets = {
            'employee': forms.Select(attrs={'class': 'form-control'}),
            'product': forms.Select(attrs={'class': 'form-control'}),
            'site': forms.Select(attrs={'class': 'form-control'}),
            'qty': forms.TextInput(attrs={'class': 'form-control'}),
            'rate': forms.TextInput(attrs={'class': 'form-control'}),
            'amount': forms.TextInput(attrs={'class': 'form-control'}),
            'msg_status': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            
        }
        
