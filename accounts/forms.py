from django import forms
from .models import CustomUser
from django.contrib.auth.forms import UserCreationForm


class SignUpForm(UserCreationForm):
    
    first_name = forms.CharField(label="First Name", max_length=30, required=False, help_text="Optional.")
    last_name = forms.CharField(label="Last Name", max_length=30, required=False, help_text="Optional.")
    email = forms.EmailField(label="E-Mail", max_length=30, required=True, help_text="Required. Use a valid email adress.")


    class Meta:
        model = CustomUser
        fields = ("first_name", "last_name", "username", "email", "password1", "password2")