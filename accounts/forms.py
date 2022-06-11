from django import forms
from .models import CustomUser
from django.contrib.auth.forms import UserCreationForm


class SignUpForm(UserCreationForm):
    
    first_name = forms.CharField(label="First Name", max_length=150, required=False, help_text="Optional.")
    last_name = forms.CharField(label="Last Name", max_length=150, required=False, help_text="Optional.")


    class Meta:
        model = CustomUser
        fields = ("first_name", "last_name", "username", "email", "password1", "password2")



