from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm

from .models import User, UserInfo
from django.shortcuts import redirect


class RegisterForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        # fields = ("username", "email")

    @staticmethod
    def account9auth():
        redirect('https://accounts.net9.org/api/authorize')


class UserInfoForm(ModelForm):
    class Meta(ModelForm):
        model = UserInfo
        fields = ("user_id_num", "name", "student_id", "id_card", "gender", "birth_date", "reading_degree", "faculty", "class_id",
                  "clothes_size", "email", "cellphone_num", "dormitory")
        # fields = ("name", "student_id")
