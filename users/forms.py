from django import forms
from .models import person

class UserForm(forms.ModelForm):
    class Meta:
        model = person
        fields = ['name']
