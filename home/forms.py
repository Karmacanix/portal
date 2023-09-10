import unicodedata

from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

UserModel = get_user_model()


class NewUserForm(UserCreationForm):
    
    class Meta:
        model = UserModel
        fields = ["username", "email", "password1", "password2"]
