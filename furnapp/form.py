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



class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['full_name', "email", 'choices', "mobile", "message"]


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('authour',  'message')