from django.urls import path

from .views import ForumPostListCreateView, ForumPostDetailView, LikePostView, ReplyCreateView

urlpatterns = [
    path('posts/', ForumPostListCreateView.as_view(), name='forum-post-list'),
    path('posts/<int:pk>/', ForumPostDetailView.as_view(), name='forum-post-detail'),
    path('posts/<int:post_id>/like/', LikePostView.as_view(), name='like-post'),
    path('posts/<int:post_id>/reply/', ReplyCreateView.as_view(), name='reply-to-post'),
]
