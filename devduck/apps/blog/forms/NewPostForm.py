from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.forms import ModelForm
from django import forms
from devduck.apps.blog.models import Post

class CreatePostForm(ModelForm):

    class Meta:
        model = Post
        fields = ['title', 'content', 'id_prog_language', 'id_grid']