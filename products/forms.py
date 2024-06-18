from django import forms
from .models import Product, Blog

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = "__all__"

class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = "__all__"


