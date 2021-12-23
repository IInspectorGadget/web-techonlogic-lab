from rest_framework import serializers
from .models import *

class NewsListSerializer(serializers.ModelSerializer):
    """Вывод списка новостей форума"""
    class Meta:
        model = News
        fields = ['title','small_text','date_pub','image','author']

class NewsDetailSerializer(serializers.ModelSerializer):
    """Вывод новости"""
    newscomments_set = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='text'
    )
    class Meta:
        model = News
        fields = ['title','small_text','date_pub','image','author','message_count','text', 'newscomments_set']

class NewsCreateSerializer(serializers.ModelSerializer):
    """Вывод новости"""
    class Meta:
        model = News
        fields = ['title','small_text','date_pub','image','author','text']

class NewsUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = ['title','small_text','image','text']

class CommentsCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewsComments
        fields = "__all__"


