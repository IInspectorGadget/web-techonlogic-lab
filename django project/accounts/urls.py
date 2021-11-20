from django.contrib.auth import views
from .views import *
from django.urls import path
from mysite import settings

app_name = 'accounts'

urlpatterns = [
    path('login/', MyLoginView.as_view(), name='login'),
    path('logout/', views.LogoutView.as_view() , name='logout'),

    path('password_change/', MyPasswordChangeView.as_view(), name='password_change'),
    path('password_change/done/', MyPasswordChangeDoneView.as_view(), name='password_change_done'),

    path('password_reset/', MyPasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', MyPasswordResetDoneView.as_view(), name='password_reset_done'),
    
    path('reset/<uidb64>/<token>/', MyPasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', MyPasswordResetCompleteView.as_view(), name='password_reset_complete'),

    path('register/', RegisterView.as_view(), name='register'),
    path('register/POST', registerPost, name='registerPost'),
]
