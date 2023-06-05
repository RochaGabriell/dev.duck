from django import forms
from django.forms import ModelForm
from devduck.apps.blog.models import Post, Grid, ProgLanguage

class CreatePostForm(ModelForm):

    class Meta:
        model = Post
        fields = ['title', 'content', 'id_prog_language', 'id_grid']

    title = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'name-heading-input',
            'placeholder': 'Título',
        })
    )

    content = forms.CharField(
        widget=forms.Textarea(attrs={
            'class': 'post-form',
            'id': 'markdown',
            'cols': '40',
            'rows': '25',
            'placeholder': 'Escreva o conteúdo do seu post aqui...',
        })
    )

    id_grid = forms.ModelChoiceField(
        queryset=Grid.objects.all(),
        widget=forms.Select(attrs={
            'class': 'button-transaction select-subjects-bottom',
            'id': 'subjects',
            'style': 'display: none;',
        })
    )

    id_prog_language = forms.ModelChoiceField(
        queryset=ProgLanguage.objects.all(),
        required=False,
        widget=forms.Select(attrs={
            'class': 'button-transaction select-subjects-bottom',
            'id': 'subjects-language',  
            'style': 'display: none;',
        })
    )


class UpdatePostForm(ModelForm):

    class Meta:
        model = Post
        fields = ['title', 'content', 'id_prog_language', 'id_grid']

    title = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'name-heading-input',
            'placeholder': 'Título',
        })
    )

    content = forms.CharField(
        widget=forms.Textarea(attrs={
            'class': 'post-form',
            'id': 'markdown',
            'cols': '40',
            'rows': '25',
            'placeholder': 'Escreva o conteúdo do seu post aqui...',
        })
    )

    id_grid = forms.ModelChoiceField(
        queryset=Grid.objects.all(),
        widget=forms.Select(attrs={
            'class': 'button-transaction select-subjects-bottom',
            'id': 'subjects',
        })
    )

    id_prog_language = forms.ModelChoiceField(
        queryset=ProgLanguage.objects.all(),
        required=False,
        widget=forms.Select(attrs={
            'class': 'button-transaction select-subjects-bottom',
            'id': 'subjects-language',
        })
    )