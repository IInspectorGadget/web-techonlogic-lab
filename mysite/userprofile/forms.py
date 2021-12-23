from django import forms 
from .models import User
from django.core.exceptions import NON_FIELD_ERRORS
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

#форма которая используется при регистрации
class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = User
        fields = ('username',)
        
#форма которая используется в интерфейсе администратора
class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = User
        fields = ('email',)

#форма пользователя основная
class UserForm(forms.ModelForm):
    username = forms.CharField(widget=forms.TextInput(attrs={"class":"formBtn", "placeholder":"Имя"}))
    email = forms.EmailField(widget=forms.TextInput(attrs={"class":"formBtn", "placeholder":"Email"}))
    password = forms.CharField(widget=forms.TextInput(attrs={"class":"formBtn", "placeholder":"Пароль", "type":"password"}))

    class Meta:
        model = User
        fields = ('username','email','password','get_news')

    def save(self, commit=True):
        """Переопределение метода save"""
        user = super(UserForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user 

#форма для редактирования данных пользователя
class ProfileEditForm(forms.ModelForm):
    addres = forms.CharField(required =False ,widget=forms.Textarea(attrs={'class':'contacts-textarea'}))
    phone = forms.CharField(required =False,error_messages={'phone': 'Please enter your name'})
    class Meta:
        model = User
        fields = { 'email', 'gender', 'phone', 'skype', 'addres','patronymic','last_name','first_name','dateBirth', 'image','get_news'}
     
    error_messages = {
        NON_FIELD_ERRORS: {
            'phone': "Введите корректный номер",
        }
    }