from django.urls import path 
from . import views
app_name = 'forum'

urlpatterns = [
    path('', views.ForumTitleView.as_view(), name='forum'),
    path('<int:id>/', views.ForumTopView.as_view(), name='forumTop'),
    path('<int:id>/<int:middle_id>', views.ForumMiddleView.as_view(), name='forumMiddle'),
]
