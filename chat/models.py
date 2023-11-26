from django.conf import settings
from django.db import models


class WorldChatMessage(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)


class DirectMessage(models.Model):
    sender = models.ForeignKey(settings.AUTH_USER_MODEL,
                               related_name='sent_dm',
                               on_delete=models.CASCADE)
    receiver = models.ForeignKey(settings.AUTH_USER_MODEL,
                                 related_name='received_dm',
                                 on_delete=models.CASCADE)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
