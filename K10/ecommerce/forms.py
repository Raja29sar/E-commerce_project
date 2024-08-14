from django import forms
from .models import Ecommerce

class EcommerceForm(forms.ModelForm):
    class Meta:
        model = Ecommerce
        fields =['name','phonenumber','email' ]