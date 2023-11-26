from django.db import models
from rest_framework import generics, permissions
from rest_framework.exceptions import ValidationError
from rest_framework.pagination import PageNumberPagination

from accounts.models import User
from .models import WorldChatMessage, DirectMessage
from .serializers import WorldChatMessageSerializer, DirectMessageSerializer


class StandardResultsSetPagination(PageNumberPagination):
    page_size = 20
    page_size_query_param = 'page_size'
    max_page_size = 100


# World Chat
class WorldChatListCreateView(generics.ListCreateAPIView):
    queryset = WorldChatMessage.objects.all().order_by('-created_at')
    serializer_class = WorldChatMessageSerializer
    permission_classes = [permissions.IsAuthenticated]
    pagination_class = StandardResultsSetPagination

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


# Direct Messaging
class DirectMessageListCreateView(generics.ListCreateAPIView):
    serializer_class = DirectMessageSerializer
    permission_classes = [permissions.IsAuthenticated]
    pagination_class = StandardResultsSetPagination

    def get_queryset(self):
        user_id = self.kwargs['user_id']
        return DirectMessage.objects.filter(
            models.Q(sender=user_id) | models.Q(receiver=user_id)
        ).order_by('-created_at')

    def perform_create(self, serializer):
        receiver = generics.get_object_or_404(User, pk=self.kwargs['user_id'])
        if receiver == self.request.user:
            raise ValidationError('You cannot send a message to yourself.')
        serializer.save(sender=self.request.user, receiver=receiver)
