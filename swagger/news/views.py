from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView, UpdateAPIView
from news.models import News
from news.serializers import CommentsCreateSerializer, NewsCreateSerializer, NewsDetailSerializer, NewsListSerializer, NewsUpdateSerializer
from rest_framework.permissions import IsAuthenticated


class NewsListView(ListAPIView):
    """Вывода списка новостей"""
    queryset = News.objects.all()
    serializer_class = NewsListSerializer

class NewsDetailView(RetrieveAPIView):
    """Вывода новости"""
    queryset = News.objects.all()
    serializer_class = NewsDetailSerializer

class NewsCreateCommentView(CreateAPIView):
    """Создание коментарев"""
    permission_classes = [IsAuthenticated]
    serializer_class = CommentsCreateSerializer

class NewsFormView(CreateAPIView):
    """Создание новости"""
    permission_classes = [IsAuthenticated]
    serializer_class = NewsCreateSerializer

class NewsEditView(UpdateAPIView, RetrieveAPIView):
    """Редактирование новости"""
    queryset = News.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = NewsUpdateSerializer
