# accounts/forms.py
from django import forms
from .models import Customer

class CustomerForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = Customer
        fields = ['username', 'email', 'first_name', 'last_name', 'password']
