from django.urls import path 
from . import views
app_name = 'profile'

urlpatterns = [

    path('<slug:username>/', views.ProfileDetailView.as_view(), name="profile"),

    path('search/Users/', views.SearchProfileView.as_view(), name="profileSearch"),
    path('<slug:username>/friends/', views.ProfileFriendsView.as_view(), name="profileFriends"),

    path('<slug:username>/edit/', views.ProfileFormView.as_view(), name ='edit'),
    path('<slug:username>/add/', views.send_friend_request, name ='add'),
    path('<slug:username>/accept/', views.accept_friend_request, name ='accept'),
    path('<slug:username>/deny/', views.deny_friend_request, name ='deny'),
    path('<slug:username>/<slug:friend>/delete/', views.delete_friend_request, name='deleteFriend'),


]
