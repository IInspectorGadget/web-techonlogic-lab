from django.urls import path 
from . import views
app_name = 'main'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('info', views.InfoView.as_view(), name='info'),
]
