from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.forms import ModelForm
from django import forms
from accounts.models import User


class UserCreationForm(UserCreationForm):

    class Meta:
        model = User
        fields = ["matriculation", "username", "email", "password"]
        widgets = {
            "matriculation": forms.TextInput(attrs={"class": "form-control"}),
            "username": forms.TextInput(attrs={"class": "form-control"}),
            "email": forms.EmailInput(attrs={"class": "form-control"}),
            "password": forms.PasswordInput(attrs={"class": "form-control"}),
        }


class UserChangeForm(UserChangeForm):

    class Meta:
        model = User
        fields = ["matriculation", "username", "email", "password"]
        widgets = {
            "matriculation": forms.TextInput(attrs={"class": "form-control"}),
            "username": forms.TextInput(attrs={"class": "form-control"}),
            "email": forms.EmailInput(attrs={"class": "form-control"}),
            "password": forms.PasswordInput(attrs={"class": "form-control"}),
        }


class LoginUser(ModelForm):

    class Meta:
        model = User
        fields = ["username", "password"]
        widgets = {
            "username": forms.TextInput(attrs={"class": "form-control"}),
            "password": forms.PasswordInput(attrs={"class": "form-control"}),
        }


class RecoveryEmail(ModelForm):

    class Meta:
        model = User
        fields = ["email"]
        widgets = {
            "email": forms.EmailInput(attrs={"class": "form-control"}),
        }


class ChangerPassword(ModelForm):

    class Meta:
        model = User
        fields = ["password"]
        widgets = {
            "password": forms.PasswordInput(attrs={"class": "form-control"}),
        }