from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

from .models import *


class RegisterUserForm(UserCreationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-input'}))
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'class': 'form-input'}))
    password1 = forms.CharField(label='Пороль', widget=forms.PasswordInput(attrs={'class': 'form-input'}))
    password2 = forms.CharField(label='Повтор пороля', widget=forms.PasswordInput(attrs={'class': 'form-input'}))

    class Meta:
        model = get_user_model()
        fields = ('username', 'email', 'password1', 'password2')
        fields = ('username', 'email', 'password1', 'password2')

class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-input'}))
    password = forms.CharField(label='Пороль', widget=forms.PasswordInput(attrs={'class': 'form-input'}))


class MessageForm(forms.ModelForm):
    message = forms.CharField(label='Введите текст', widget=forms.TextInput(attrs={'class': 'message-input'}))
    
    class Meta: 
        model = Message # get_user_model()
        fields = ('message',)


# class UserForm(forms.ModelForm):
#     read = forms.BooleanField(label='Добавить', widget=forms.BooleanField())

#     class Meta:
#         model = get_user_model()
#         fields = ('read',)