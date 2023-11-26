from rest_framework import serializers

from .models import WorldChatMessage, DirectMessage


class WorldChatMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorldChatMessage
        fields = ['id', 'user', 'message', 'created_at']
        read_only_fields = ['user']


class DirectMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = DirectMessage
        fields = ['id', 'sender', 'receiver', 'message', 'created_at']
        read_only_fields = ['sender', 'receiver']
