from django.urls import path 
from . import views
app_name = 'forum'

urlpatterns = [
    path('', views.ForumTitleView.as_view(), name='forum'),
    path('<int:pk>/', views.ForumTopView.as_view(), name='forumTop'),
    path('<int:id>/<int:middle_id>', views.ForumMiddleView.as_view(), name='forumMiddle'),
    path('<int:id>/<int:middle_id>/create/', views.ForumMessageView.as_view(), name='forumMiddle'),
]
