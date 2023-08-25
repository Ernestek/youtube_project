from django.contrib import admin

from parser_app.models import Video, Channels, Keywords, UserTariff


@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    list_display = ('video_id', 'video_name', 'channel_id', 'channel_title', 'description', 'kind', 'etag', 'id_kind',
                    'published_at', 'thumbnails_default', 'thumbnails_medium', 'thumbnails_high',
                    'live_broadcast_content', 'publish_time')


@admin.register(Channels)
class ChannelsAdmin(admin.ModelAdmin):
    list_display = ('channel_id', 'channel_title', 'description', 'kind', 'etag', 'id_kind', 'published_at',
                    'thumbnails_default', 'thumbnails_medium', 'thumbnails_high', 'live_broadcast_content',
                    'publish_time')


@admin.register(Keywords)
class KeywordsAdmin(admin.ModelAdmin):
    list_display = ('name', 'status')


@admin.register(UserTariff)
class UserTariffAdmin(admin.ModelAdmin):
    list_display = ('user', 'remaining_searches')
