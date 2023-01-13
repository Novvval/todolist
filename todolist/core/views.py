from django.contrib.auth import login, logout
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import ensure_csrf_cookie
from rest_framework import status
from rest_framework.generics import CreateAPIView, RetrieveUpdateDestroyAPIView, UpdateAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from .models import User
from .serializers import CreateUserSerializer, LoginSerializer, ProfileSerializer, UpdatePasswordSerializer


# Create your views here.


class SignupView(CreateAPIView):
    """Вью для регистрации пользователя"""
    serializer_class = CreateUserSerializer
    permission_classes = (AllowAny,)


class LoginView(CreateAPIView):
    """Вью для логина пользователя"""
    serializer_class = LoginSerializer
    permission_classes = (AllowAny,)

    def perform_create(self, serializer):
        login(request=self.request, user=serializer.save())


class ProfileView(RetrieveUpdateDestroyAPIView):
    """Для для просмотра и редактирования данных пользователя"""
    serializer_class = ProfileSerializer
    queryset = User.objects.all()
    permission_classes = (IsAuthenticated,)

    def get_object(self):
        return self.request.user

    def delete(self, request, *args, **kwargs):
        logout(request)
        return Response(status.HTTP_204_NO_CONTENT)


class UpdatePasswordView(UpdateAPIView):
    serializer_class = UpdatePasswordSerializer
    permission_classes = (IsAuthenticated,)

    def get_object(self):
        return self.request.user

