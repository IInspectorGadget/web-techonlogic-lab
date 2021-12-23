
from forum.models import  ForumMiddle, ForumTitle, ForumTop
from forum.serializers import ForumMessageSerializer, ForumTitleSerializer,ForumTopSerializer,ForumMiddleSerializer
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView


class ForumTitleView(ListAPIView):
    """Вывод загаловков форума"""
    queryset = ForumTitle.objects.all()
    serializer_class = ForumTitleSerializer

class ForumTopView(RetrieveAPIView):
    "Вывод тем форума"
    queryset = ForumTop.objects.all()
    serializer_class = ForumTopSerializer

class ForumMiddleView(ListAPIView):
    queryset = ForumMiddle.objects.all()
    serializer_class = ForumMiddleSerializer

class ForumMessageView(CreateAPIView):
    serializer_class = ForumMessageSerializer


