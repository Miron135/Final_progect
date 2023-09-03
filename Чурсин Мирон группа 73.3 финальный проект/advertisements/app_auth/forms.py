from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegistrationForm(UserCreationForm):
    first_name = forms.CharField(label=('Name'), max_length=32)
    last_name = forms.CharField(label=('Surname'), max_length=32)
    email = forms.EmailField(max_length=64)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')
