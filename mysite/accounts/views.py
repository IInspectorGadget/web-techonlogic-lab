from django.shortcuts import render
from django.contrib.auth.views import LoginView
from django import forms 
from .forms import MyAuthenticationForm
from userprofile.forms import UserForm
from django.http import HttpResponseRedirect
from django.views.generic.base import View
from django.urls import reverse, reverse_lazy
from django.contrib.auth import views as a
from accounts.forms import MyPasswordChangeForm, MySetPasswordForm

class MyLoginView(LoginView):
    form_class = MyAuthenticationForm
  
class MyRegisterView():
    pass

class MyPasswordResetView(a.PasswordResetView):
    success_url = reverse_lazy('accounts:password_reset_done')
    title = 'Сброс пароля'

class MyPasswordResetDoneView(a.PasswordResetDoneView):
    title = 'Сброс пароля отправлен'

class MyPasswordResetConfirmView(a.PasswordResetConfirmView):
    success_url = reverse_lazy('accounts:password_reset_complete')
    title = 'Введите новый пароль'
    form_class = MySetPasswordForm

class MyPasswordResetCompleteView(a.PasswordResetCompleteView):
    title = 'Пароль успешно сброшен'

class MyPasswordChangeView(a.PasswordChangeView):
    success_url = reverse_lazy('accounts:password_change_done')
    title = 'Изменение пароля'
    form_class = MyPasswordChangeForm

class MyPasswordChangeDoneView(a.PasswordChangeDoneView):
    title = 'Пароль успешно изменён'

class RegisterView(View):
    def get(self, request):
        userform = UserForm()
        context = {
            "form": userform
        }
        return render(request,'registration/registerForm.html', context)

def registerPost(request):
    # получаю данные и файлы  из формы
    userform = UserForm(request.POST, request.FILES)
    # проверяю валидность данных
    if userform.is_valid():
        # если есть файл с именем image то присваивается название файла
        userform.save(commit=True)
        return HttpResponseRedirect(reverse('accounts:login'))
    else:
        return render(request, 'registration/registerForm.html', {'form': userform})