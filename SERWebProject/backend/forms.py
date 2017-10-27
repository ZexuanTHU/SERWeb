from django.contrib.auth.forms import UserCreationForm
from .models import User
from django.shortcuts import redirect


class RegisterForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        # fields = ("username", "email")

    @staticmethod
    def account9auth():
        redirect('https://accounts.net9.org/api/authorize')

