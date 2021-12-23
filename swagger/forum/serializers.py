from rest_framework import serializers
from .models import *


class ForumTitleSerializer(serializers.ModelSerializer):
    """Вывод загаловков форума"""
    forumTitle = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='name'
    )

    class Meta:
        model = ForumTitle
        fields = ['name','forumTitle']

class ForumTopSerializer(serializers.ModelSerializer):
    """Вывод тем форума"""
    forumtop = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='name'
    )
    class Meta:
        model = ForumTop
        fields = ['name','image','post_count', 'forumtop']




class ForumMiddleSerializer(serializers.ModelSerializer):
    """Вывод под-тем форума"""
    forummiddle = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='message'
    )


    class Meta:
        model = ForumMiddle
        fields = ('name','user','date_create','post_count','forummiddle')

class ForumMessageSerializer(serializers.ModelSerializer):
    """Вывод сообщений форума"""
    class Meta:
        model = ForumMessage
        fields = "__all__"