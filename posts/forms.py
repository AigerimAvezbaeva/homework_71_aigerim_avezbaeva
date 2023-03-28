from django import forms
from django import forms
from django.forms.widgets import Textarea, HiddenInput, Input

from posts.models import Post, Comment


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('description', 'image')


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('text',)
        labels = {'text': ''}


