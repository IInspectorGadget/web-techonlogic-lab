from django.contrib import admin
from django.urls import path
from . import views
app_name="may"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('TelegramPassword', views.telegramPassword, name='TelegramPassword'),
    path('addNews', views.addNews, name='TelegramPassword'),
]
