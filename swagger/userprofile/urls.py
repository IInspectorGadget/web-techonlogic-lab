from django.urls import path 
from . import views
app_name = 'profile'

urlpatterns = [
    path('<int:pk>/', views.ProfileDetailView.as_view(), name="profile"),
    path('search/Users/', views.SearchProfileView.as_view(), name="profileSearch"),
    path('<int:pk>/edit/', views.ProfileFormView.as_view(), name ='edit'),
]
