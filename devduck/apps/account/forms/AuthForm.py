from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.forms import ModelForm
from django import forms
from devduck.apps.account.models.User import User


class UserCreationForm(UserCreationForm):

    class Meta:
        model = User
        fields = ["matriculation", "username", "email"]
        widgets = {
            "matriculation": forms.TextInput(attrs={"class": "form-control"}),
            "username": forms.TextInput(attrs={"class": "form-control"}),
            "email": forms.EmailInput(attrs={"class": "form-control"}),
        }

    def clean_username(self) -> str:
        username = self.cleaned_data["username"]
        if not username.isalnum():
            raise forms.ValidationError("Nome de Usuário não é alfanumérico")
        return username

    def clean_matriculation(self):
        matriculation = self.cleaned_data["matriculation"]
        if len(matriculation) != 15:
            raise forms.ValidationError("Matrícula inválida")
        return matriculation


class UserChangeForm(UserChangeForm):

    class Meta:
        model = User
        fields = ["username", "email"]
        widgets = {
            "username": forms.TextInput(attrs={"class": "form-control"}),
            "email": forms.EmailInput(attrs={"class": "form-control"}),
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