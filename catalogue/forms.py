from django import forms
from django.forms.widgets import HiddenInput

from catalogue.models import Service


class ServiceNewForm(forms.ModelForm):
    
    class Meta:
        model = Service
        fields = ('name', 'category', 'cost')
        widgets = {'category': HiddenInput()}
        

class ServiceForm(forms.ModelForm):
    
    class Meta:
        model = Service
        fields = ('name', 'category', 'cost')
