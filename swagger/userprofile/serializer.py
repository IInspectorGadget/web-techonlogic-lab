from rest_framework import serializers
from .models import *

class UserDetailSerializer(serializers.ModelSerializer):
    """Вывод информации о пользователе"""
    user_set = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='username'
    )
    class Meta:
        model = User
        fields = ['user_set','image','email', 'gender', 'phone', 'skype', 'addres','patronymic','last_name','first_name','dateBirth', 'image']

class UserListSerializer(serializers.ModelSerializer):
    """Вывод списка пользователей"""
    class Meta:
        model = User
        fields = ['image','username']


