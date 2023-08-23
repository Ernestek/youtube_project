from django.db import models


class Keywords(models.Model):
    name = models.CharField(max_length=512)
    status = models.CharField(max_length=50, default='New')


class Video(models.Model):
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
