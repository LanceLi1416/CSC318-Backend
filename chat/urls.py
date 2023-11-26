from django.urls import path

from .views import WorldChatListCreateView, DirectMessageListCreateView

urlpatterns = [
    path('world/', WorldChatListCreateView.as_view(), name='world-chat'),
    path('dm/<int:user_id>/', DirectMessageListCreateView.as_view(), name='direct-message'),
]
