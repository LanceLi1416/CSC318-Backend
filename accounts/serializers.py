from django.contrib.auth.hashers import make_password
from rest_framework import serializers

from .models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password', 'nickname', 'profile_picture', 'bio',
                  'following']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def validate_password(self, value: str) -> str:
        return make_password(value)
