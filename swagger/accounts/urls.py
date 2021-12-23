from django.contrib.auth import views
from .views import *
from django.urls import path

app_name = 'accounts'

urlpatterns = [
    path('login/', MyLoginView.as_view(), name='login'),
    path('logout/', views.LogoutView.as_view() , name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
]
