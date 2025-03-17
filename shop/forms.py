from django import forms
from phonenumber_field.formfields import PhoneNumberField
from shop.models import Customers
from django.shortcuts import get_object_or_404


class CustomersModelForm(forms.ModelForm):
    class Meta:
        model = Customers
        exclude = ()



