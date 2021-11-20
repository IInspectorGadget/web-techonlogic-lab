from django.urls import path 
from . import views
from django.contrib.auth.decorators import login_required
from news.models import LikeDislike, News, NewsComments
app_name = 'news'

urlpatterns = [
    path('', views.NewsListView.as_view(), name='news'),
    path('<int:id>', views.NewsDetailView.as_view(), name='newsDetail'),
    path('add', views.NewsFormView.as_view(), name='newsAdd'),
    path('<int:id>/edit', views.NewsEditView.as_view(), name='newsEdit'),

    path('<int:pk>/like/', login_required(views.VotesView.as_view(model=News, vote_type=LikeDislike.LIKE)), name='article_like'),
    path('<int:pk>/dislike/', login_required(views.VotesView.as_view(model=News, vote_type=LikeDislike.DISLIKE)), name='article_dislike'),

    path('comments/<int:pk>/like-comment/', login_required(views.VotesView.as_view(model=NewsComments, vote_type=LikeDislike.LIKE)), name='article_like'),
    path('comments/<int:pk>/dislike-comment/', login_required(views.VotesView.as_view(model=NewsComments, vote_type=LikeDislike.DISLIKE)), name='article_dislike'),

]
