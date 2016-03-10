from django.contrib.auth.forms import UserCreationForm
from django import forms
from theonsapp.models import City


class NewUserCreation(UserCreationForm):
    home_city = forms.ModelChoiceField(queryset=City.objects.all())
