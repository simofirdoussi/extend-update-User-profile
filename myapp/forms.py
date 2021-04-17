
from django import forms
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django.contrib.auth import get_user_model
from django.forms import fields
from .models import User

class ProfileForm(UserChangeForm):
        
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'image', 'description')