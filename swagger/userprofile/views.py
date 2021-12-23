from userprofile.models import  User
from rest_framework.generics import ListAPIView, RetrieveAPIView, UpdateAPIView
from userprofile.serializer import UserDetailSerializer, UserListSerializer

class ProfileDetailView(RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserDetailSerializer

class ProfileFormView(UpdateAPIView,RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserDetailSerializer

class SearchProfileView(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserListSerializer

