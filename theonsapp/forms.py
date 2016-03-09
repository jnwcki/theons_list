from django.contrib.auth.forms import UserCreationForm
from django import forms


class NewUserCreation(UserCreationForm):
    screen_name = forms.CharField()
