from re import T
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

    
class UserEditForm(UserChangeForm):
    email = forms.EmailField(required=True)
    password1 = forms.CharField(required=True, label='Change Password', widget=forms.PasswordInput)
    password2 = forms.CharField(required=True, label='Confirm Password', widget=forms.PasswordInput)
    user = forms.CharField(label='Add / Change username')

class Meta:
    model= User
    fields= ("username", "email", "password1", "password2")
    help_texts={k:"" for k in fields}    

class Edit_profile_form(forms.Form):
    user = forms.CharField (label="User name")
    address = forms.CharField(label="Address") 
    phone = forms.CharField(label="Phone number")
    image = forms.ImageField()
