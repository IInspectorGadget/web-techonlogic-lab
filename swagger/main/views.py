from django.shortcuts import render
from main.serializer import MainSerializer
from news.models import News
from rest_framework.generics import ListAPIView

class IndexView(ListAPIView):
    queryset = News.objects.filter()
    serializer_class = MainSerializer