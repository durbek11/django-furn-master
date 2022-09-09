from tkinter import Widget
from django import forms
from django.contrib.auth.forms import UserCreationForm, UsernameField
from django.contrib.auth import get_user_model
from dataclasses import fields
from .models import *

User = get_user_model()


class Registration(UserCreationForm):
    class Meta:
        model = User
        fields = ["first_name", "last_name", "email", "password1", "password2"]



class UpdateUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', "email"]
        widgets = {
            'first_name': forms.TextInput(attrs={"class": "form-control", "placeholder": "First Name", "id": "firstname"}),
            'last_name': forms.TextInput(attrs={"class": "form-control", "placeholder": "Last Name", "id": "lastname"}),
            'email': forms.EmailInput(attrs={"class": 'form-control w-75', "placeholder": "Email", "id": "email"})
        }


class UpdateProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image', 'bio', 'card_number', 'address', 'mobile_number']
        # fields = '__all__'

class ProductRateForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['star_1', "star_2", 'star_3', 'star_4', 'star_5']
        widgets = {
            'star_1': forms.TextInput(attrs={"id": 'star5', 'name':'rate', "value":'5', "type":"radio"}),
            'star_2': forms.TextInput(attrs={"id": 'star4', 'name':'rate', "value":'4', "type":"radio"}),
            'star_3': forms.TextInput(attrs={"id": 'star3', 'name':'rate', "value":'3', "type":"radio"}),
            'star_4': forms.TextInput(attrs={"id": 'star2', 'name':'rate', "value":'2', "type":"radio"}),
            'star_5': forms.TextInput(attrs={"id": 'star1', 'name':'rate', "value":'1', "type":"radio"}),
        }


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['full_name', "email", 'choices', "mobile", "message"]