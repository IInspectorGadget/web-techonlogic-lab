from django.contrib.auth.forms import AuthenticationForm, UsernameField, SetPasswordForm, PasswordChangeForm
from django import forms
from news.models import User


class MyAuthenticationForm(AuthenticationForm):
    password = forms.CharField(
        label= ("Password"),
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'current-password', "class":"formBtn", "placeholder":"Пароль"}),
    )
    username = UsernameField(widget=forms.TextInput(attrs={'autofocus': True, "class":"formBtn", "placeholder":"Логин"}))
   
class MySetPasswordForm(SetPasswordForm):
    error_messages = {
        'password_mismatch': 'Два поля пароля не совпадают.',
    }
    
class MyPasswordChangeForm(PasswordChangeForm):
    error_messages = {
        'password_mismatch': 'Два поля пароля не совпадают.',
        'password_incorrect': "Ваш старый пароль не верный. Введите правильный пароль.",
    }