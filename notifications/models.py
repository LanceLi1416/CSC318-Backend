from django.conf import settings
from django.db import models


class Notification(models.Model):
    # Types of notifications
    REPLY = 'reply'
    DIRECT_MESSAGE = 'dm'
    SYSTEM_MESSAGE = 'system'
    NOTIFICATION_TYPES = [
        (REPLY, 'Reply'),
        (DIRECT_MESSAGE, 'Direct Message'),
        (SYSTEM_MESSAGE, 'System Message'),
    ]

    recipient = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='notifications',
                                  on_delete=models.CASCADE)
    message = models.TextField()
    notification_type = models.CharField(max_length=10, choices=NOTIFICATION_TYPES)
    created_at = models.DateTimeField(auto_now_add=True)
    read = models.BooleanField(default=False)
    link = models.URLField(max_length=200, blank=True, null=True,
                           help_text="URI to the related resource")

    def __str__(self):
        return f'Notification({self.get_notification_type_display()}) to {self.recipient.username}'
