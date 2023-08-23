from django.db import models


class Keywords(models.Model):
    name = models.CharField(max_length=512)
    status = models.CharField(max_length=50, default='New')


class Video(models.Model):
    video_id = models.CharField(max_length=512, unique=True)
    video_name = models.CharField(max_length=512, null=True, blank=True)
    channel_id = models.CharField(max_length=512, null=True, blank=True)
    channel_title = models.CharField(max_length=512, null=True, blank=True)


class Channels(models.Model):
    channel_id = models.CharField(max_length=512, unique=True)
    channel_title = models.CharField(max_length=512, null=True, blank=True)
    description = models.TextField()
