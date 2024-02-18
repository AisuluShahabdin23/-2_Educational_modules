from django.contrib.auth.hashers import make_password
from rest_framework import serializers
from module.serializers import ModuleSerializer
from users.models import User
from users.validators import EmailValidator


class UserSerializer(serializers.ModelSerializer):
    """ Сериализатор пользователя (полное отображение данных) """
    module = ModuleSerializer(source='id_users', read_only=True, many=True)

    class Meta:
        model = User
        fields = ("id", "email", "first_name", "last_name", "phone", "country",
                  "city", "roles", "module", "password", )
        validators = [
            EmailValidator(field="email")
        ]

    def validate_password(self, value: str) -> str:
        return make_password(value)


class UserPublishedSerializer(serializers.ModelSerializer):
    """ Сериализатор пользователя (ограниченное отображение данных) """
    class Meta:
        model = User
        fields = ("id", "email", "first_name", "last_name", )
