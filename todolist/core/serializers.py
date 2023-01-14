from django.contrib.auth import authenticate
from django.contrib.auth.hashers import make_password
from django.contrib.auth.password_validation import validate_password
from django.views.decorators.csrf import csrf_exempt
from rest_framework import serializers
from rest_framework.exceptions import ValidationError, AuthenticationFailed, NotAuthenticated

from .models import User


class PasswordField(serializers.CharField):
    """"Сериализатор пароля"""

    def __init__(self, **kwargs):
        kwargs["style"] = {"input": "password"}
        kwargs.setdefault("write_only", True)
        super().__init__(**kwargs)
        self.validators.append(validate_password)


class CreateUserSerializer(serializers.ModelSerializer):
    """Сериализатор создания пользователя при регистрации, валидация повторного пароля и переопределение метода
    create модели ModelSerializer"""
    password = PasswordField(required=True)
    password_repeat = PasswordField(required=True)

    class Meta:
        model = User
        fields = ["id", "password", "password_repeat", "username", "first_name", "last_name"]

    def validate(self, attrs: dict):
        if attrs["password"] != attrs["password_repeat"]:
            raise ValidationError("Password must match")
        elif len(attrs["password"]) < 8:
            raise ValidationError("Password must be more than 8 characters")
        return attrs

    def create(self, validated_data: dict):
        del validated_data["password_repeat"]
        validated_data["password"] = make_password(validated_data["password"])
        return super().create(validated_data)


class LoginSerializer(serializers.ModelSerializer):
    """Сериализатор для логина"""
    password = PasswordField(required=True)
    username = serializers.CharField(required=True)

    class Meta:
        model = User
        fields = ["password", "username"]

    def create(self, validated_data: dict):
        if not (user := authenticate(
                username=validated_data["username"],
                password=validated_data["password"]
        )):
            raise AuthenticationFailed
        return user


class ProfileSerializer(serializers.ModelSerializer):
    """Сериализатор для действий по профилю"""
    class Meta:
        model = User
        fields = ["id", "username", "first_name", "last_name", "email"]


class UpdatePasswordSerializer(serializers.Serializer):
    """Сериализатор для обновления пароля"""
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    old_password = PasswordField(required=True)
    new_password = PasswordField(required=True)

    def create(self, validated_data: dict) -> User:
        raise NotImplementedError

    def update(self, instance: User, validated_data: dict) -> User:
        instance.password = make_password(validated_data["new_password"])
        instance.save(update_fields=("password",))
        return instance
