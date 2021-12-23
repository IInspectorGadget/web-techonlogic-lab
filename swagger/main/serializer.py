from rest_framework import serializers
from news.models import News

class MainSerializer(serializers.ModelSerializer):
    """Вывод списка новостей и форума"""

    class Meta:
        model = News
        fields = ['title']