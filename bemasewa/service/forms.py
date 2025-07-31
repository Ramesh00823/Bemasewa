from django import forms
from .models import Application, PanCardApplication,LifeInsuranceApplication

class ApplicationForm(forms.ModelForm):
    class Meta:
        model = Application
        fields = ['full_name', 'document']

class PanCardApplicationForm(forms.ModelForm):
    class Meta:
        model = PanCardApplication
        exclude = ['user', 'status', 'rejection_note']
        widgets = {
            'date_of_birth': forms.DateInput(attrs={'type': 'date'}),
        }

class LifeInsuranceForm(forms.ModelForm):
    class Meta:
        model = LifeInsuranceApplication
        exclude = [ 'status']
        widgets = {
            'date_of_birth': forms.DateInput(attrs={'type': 'date'}),
        }
