from django.forms import ModelForm, ClearableFileInput
from .models import Post, Image, File, Video

class PostForm(ModelForm):

    class meta:
        model = Post
        fields = ["title", "text", "puplished"]