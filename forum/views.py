from django.shortcuts import get_object_or_404
from rest_framework import generics, permissions, status
from rest_framework.response import Response

from notifications.models import Notification
from .models import ForumPost, Reply
from .serializers import ForumPostSerializer, ReplySerializer


class ForumPostListCreateView(generics.ListCreateAPIView):
    queryset = ForumPost.objects.all()
    serializer_class = ForumPostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class ForumPostDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ForumPost.objects.all()
    serializer_class = ForumPostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class LikePostView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, post_id):
        post = get_object_or_404(ForumPost, id=post_id)
        if request.user in post.likes.all():
            post.likes.remove(request.user)
        else:
            post.likes.add(request.user)
        return Response(status=status.HTTP_200_OK)


class ReplyCreateView(generics.CreateAPIView):
    queryset = Reply.objects.all()
    serializer_class = ReplySerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        post = get_object_or_404(ForumPost, id=self.kwargs['post_id'])
        serializer.save(author=self.request.user, post=post)

        # Create a notification for the post author
        if self.request.user != post.author:
            post.author.notifications.create(
                message=f'{self.request.user.username} replied to your post "{post.title}"',
                notification_type=Notification.REPLY,
                link=f'/posts/{post.id}/'
            )
