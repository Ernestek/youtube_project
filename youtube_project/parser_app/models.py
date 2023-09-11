from django.db import models
from django.contrib.auth.models import User


class Keywords(models.Model):
    name = models.CharField(max_length=512)
    status = models.CharField(max_length=50, default='New')


class Video(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='video')
    video_id = models.CharField(max_length=512, unique=True)
    video_name = models.CharField(max_length=512, null=True, blank=True)
    channel_id = models.CharField(max_length=512, null=True, blank=True)
    channel_title = models.CharField(max_length=512, null=True, blank=True)
    description = models.TextField()
    kind = models.CharField(max_length=256, null=True, blank=True)
    etag = models.CharField(max_length=256, null=True, blank=True)
    id_kind = models.CharField(max_length=256, null=True, blank=True)
    published_at = models.CharField(max_length=256, null=True, blank=True)
    thumbnails_default = models.CharField(max_length=512, null=True, blank=True)
    thumbnails_medium = models.CharField(max_length=512, null=True, blank=True)
    thumbnails_high = models.CharField(max_length=512, null=True, blank=True)
    live_broadcast_content = models.CharField(max_length=256, null=True, blank=True)
    publish_time = models.CharField(max_length=256, null=True, blank=True)


class Channels(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='channels')
    channel_id = models.CharField(max_length=512, unique=True)
    channel_title = models.CharField(max_length=512, null=True, blank=True)
    description = models.TextField()
    kind = models.CharField(max_length=256, null=True, blank=True)
    etag = models.CharField(max_length=256, null=True, blank=True)
    id_kind = models.CharField(max_length=256, null=True, blank=True)
    published_at = models.CharField(max_length=256, null=True, blank=True)
    thumbnails_default = models.CharField(max_length=512, null=True, blank=True)
    thumbnails_medium = models.CharField(max_length=512, null=True, blank=True)
    thumbnails_high = models.CharField(max_length=512, null=True, blank=True)
    live_broadcast_content = models.CharField(max_length=256, null=True, blank=True)
    publish_time = models.CharField(max_length=256, null=True, blank=True)


class UserTariff(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='user_tariff')
    remaining_searches = models.PositiveIntegerField(default=10)  # Начальное количество доступных запросов

    def decrement_search_limit(self):
        if self.remaining_searches > 0:
            self.remaining_searches -= 1
            self.save()

    def is_search_limit_exceeded(self):
        return self.remaining_searches <= 0

    def __str__(self):
        return f'User: {self.user.username}, Remaining'
