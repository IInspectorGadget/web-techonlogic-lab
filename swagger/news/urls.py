from django.urls import path 
from . import views
app_name = 'news'

urlpatterns = [
    path('', views.NewsListView.as_view(), name='news'),
    path('<int:pk>', views.NewsDetailView.as_view(), name='newsDetail'),
    path('<int:pk>/create', views.NewsCreateCommentView.as_view(), name='newsDetailcreateComment'),
    path('add', views.NewsFormView.as_view(), name='newsAdd'),
    path('<int:pk>/edit', views.NewsEditView.as_view(), name='newsEdit'),
]
