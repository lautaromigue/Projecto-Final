from re import T
from unicodedata import name
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from django import forms

class User_registration_form(UserCreationForm):
    email = forms.EmailField(required=True)
    password1: forms.CharField(label="Password", widget= forms.PasswordInput)
    password2: forms.CharField(label="Password confirmation", widget=forms.PasswordInput)
    
    class Meta: 
        model= User
        fields= ("username", "email", "password1", "password2")
        help_texts={k:"" for k in fields}    

    
   

class Edit_profile_form(forms.Form):
    name = forms.CharField (label="User name")
    address = forms.CharField(label="Address") 
    phone = forms.CharField(label="Phone number")
    description = forms.CharField(required=False, label='Descripción')
    image = forms.ImageField(required=False)
    website = forms.CharField(required=False, label='WebSite')
