from django import forms
from .models import Item, Purchase, Sales, Customer
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class ItemForm(forms.ModelForm):

    class Meta:
        model = Item
        fields = '__all__'

class PurchaseForm(forms.ModelForm):

    class Meta:
        model = Purchase
        fields = '__all__'

class SalesForm(forms.ModelForm):

    class Meta:
        model = Sales
        fields = '__all__'

class RegisterForm(UserCreationForm):

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class CustomerForm(forms.ModelForm):

    class Meta:
        model = Customer
        fields = '__all__'
        exclude = ['user']