from django.contrib import admin

from parser_app.models import Video, Channels, Keywords


@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    list_display = ('video_id', 'video_name', 'channel_id', 'channel_title')


@admin.register(Channels)
class ChannelsAdmin(admin.ModelAdmin):
    list_display = ('channel_id', 'channel_title', 'description')


@admin.register(Keywords)
class KeywordsAdmin(admin.ModelAdmin):
    list_display = ('name', 'status')
