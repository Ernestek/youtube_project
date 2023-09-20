import requests

from modules.load_django import *
from parser_app.models import Channels


def youtube_search_channels(query: str, user, language=None, region_code=None, topic_id=None,
                            count=50, page_token=None, channel_type='any', safe_search='moderate',
                            date_from=None, date_to=None):
    base_url = "https://www.googleapis.com/youtube/v3/search"

    params = {
        'key': 'AIzaSyAllyDaunz128tfr8mhdDFJX_x-vC5d2q8',
        'q': query,
        'type': 'channel',
        'part': 'id,snippet',
        'maxResults': count,
        'relevanceLanguage': language,
        'regionCode': region_code,
        'topicId': topic_id,
        'channel_type': channel_type,
        'safe_search': safe_search,
        'pageToken': page_token,
    }
    if date_from and date_from.strip() != 'None':
        params['publishedAfter'] = date_from + 'T00:00:00Z'
    if date_to and date_to != 'None':
        params['publishedBefore'] = date_to + 'T00:00:00Z'
    response = requests.get(base_url, params=params)
    data = response.json()
    channels = []
    for item in data.get('items', []):
        kind = item['kind']
        etag = item['etag']
        id_kind = item['id']['kind']
        published_at = item['snippet']['publishedAt']
        thumbnails_default = item['snippet']['thumbnails']['default']['url']
        thumbnails_medium = item['snippet']['thumbnails']['medium']['url']
        thumbnails_high = item['snippet']['thumbnails']['high']['url']
        live_broadcast_content = item['snippet']['liveBroadcastContent']
        publish_time = item['snippet']['publishTime']
        channel_id = item['id']['channelId']
        channel_title = item['snippet']['title']
        description = item['snippet']['description']
        channels.append({
            'channel_id': channel_id,
            'channel_title': channel_title,
            'description': description,
        })
        Channels.objects.get_or_create(
            channel_id=channel_id,
            defaults={
                'user': user,
                'channel_title': channel_title,
                'description': description,
                'kind': kind,
                'etag': etag,
                'id_kind': id_kind,
                'published_at': published_at,
                'thumbnails_default': thumbnails_default,
                'thumbnails_medium': thumbnails_medium,
                'thumbnails_high': thumbnails_high,
                'live_broadcast_content': live_broadcast_content,
                'publish_time': publish_time,
            }
        )
    return {'channels': channels, 'next_page': data.get('nextPageToken')}


def main():
    query = 'dota '
    language = 'en'
    region_code = 'US'
    topic_id = '/m/04rlf'

    channels = youtube_search_channels(query, language, region_code, topic_id, date_from='2022-10-10')
    for channel in channels['channels']:
        print(channel)
        ...


if __name__ == '__main__':
    main()
