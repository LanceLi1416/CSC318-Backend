from rest_framework import generics
from rest_framework import permissions
from rest_framework import views, status
from rest_framework.response import Response

from .models import User
from .serializers import UserSerializer


class UserListCreateView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class FollowUserView(views.APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, user_id):
        try:
            user_to_follow = User.objects.get(pk=user_id)
            # Cannot follow yourself
            if user_to_follow == request.user:
                return Response(status=status.HTTP_400_BAD_REQUEST)
            request.user.following.add(user_to_follow)
            return Response(status=status.HTTP_200_OK)
        except User.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, user_id):
        try:
            user_to_unfollow = User.objects.get(pk=user_id)
            request.user.following.remove(user_to_unfollow)
            return Response(status=status.HTTP_204_NO_CONTENT)
        except User.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
