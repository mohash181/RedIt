from django.forms import ModelForm, ClearableFileInput
from .models import Post
from django import forms


class PostForm(forms.Form):

    title = forms.CharField(max_length=250, required=True)
    text = forms.CharField(widget=forms.Textarea, required=True)


    class Meta:
        model = Post
        fields = ["title", "text"]