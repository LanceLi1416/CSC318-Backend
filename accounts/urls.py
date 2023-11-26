from django.urls import path

from .views import UserListCreateView, UserDetailView, FollowUserView

app_name = 'accounts'

urlpatterns = [
    path('users/', UserListCreateView.as_view(), name='user-list-create'),
    path('users/<int:pk>/', UserDetailView.as_view(), name='user-detail'),
    path('users/<int:user_id>/follow/', FollowUserView.as_view(), name='follow-user'),
]
