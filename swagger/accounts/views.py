from rest_framework.views import APIView
from django.contrib.auth.models import update_last_login
from accounts.serializers import LoginSerializers, UserSerializer, updatePassword 
from django.contrib.auth import views as a
from rest_framework.generics import CreateAPIView,  UpdateAPIView
from django.contrib.auth import get_user_model
from rest_framework import permissions 
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework import status

class RegisterView(CreateAPIView):
    model = get_user_model()
    permission_classes = [permissions.AllowAny]
    serializer_class = UserSerializer

class MyLoginView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = LoginSerializers(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        update_last_login(None, user)
        token, created = Token.objects.get_or_create(user=user)
        return Response({"status": status.HTTP_200_OK, "Token": token.key})

class MyPasswordResetView(UpdateAPIView):
    model = get_user_model()
    queryset = model.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = updatePassword

