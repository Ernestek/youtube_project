import requests

from modules.load_django import *
from parser_app.models import Video


def youtube_search_video(query: str, language=None, region_code=None, category_id=None, topic_id=None,
                         count=50, page_token=None, video_caption='any', video_definition='any',
                         video_embeddable='any', video_paid_product_placement='any', video_syndicated='any',
                         video_type='any', video_license='any', video_dimension='any', date_from=None, date_to=None):
    base_url = "https://www.googleapis.com/youtube/v3/search"

    params = {
        'key': 'AIzaSyAllyDaunz128tfr8mhdDFJX_x-vC5d2q8',
        'q': query,
        'type': 'video',
        'part': 'id,snippet',
        'maxResults': count,
        'relevanceLanguage': language,
        'regionCode': region_code,
        'videoCategoryId': category_id,
        'topicId': topic_id,
        'video_caption': video_caption,
        'video_definition': video_definition,
        'video_embeddable': video_embeddable,
        'video_paid_product_placement': video_paid_product_placement,
        'video_syndicated': video_syndicated,
        'video_type': video_type,
        'video_license': video_license,
        'video_dimension': video_dimension,
        # 'publishedAfter': date_from,
        # 'publishedBefore': date_to,
        'pageToken': page_token
    }
    if date_from:
        params['publishedAfter'] = date_from + 'T00:00:00Z'
    if date_to:
        params['publishedBefore'] = date_to + 'T00:00:00Z'
    response = requests.get(base_url, params=params)
    data = response.json()

    videos = []
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
        video_id = item['id']['videoId']
        channel_id = item['snippet']['channelId']
        channel_title = item['snippet']['channelTitle']
        title = item['snippet']['title']
        description = item['snippet']['description']

        # videos.append({
        #     'video_id': video_id,
        #     'video_name': title,
        #     'channel_id': channel_id,
        #     'channel_title': channel_title,
        # })
        Video.objects.get_or_create(
            video_id=video_id,
            defaults={
                'video_name': title,
                'channel_id': channel_id,
                'channel_title': channel_title,
                'kind': kind,
                'etag': etag,
                'id_kind': id_kind,
                'published_at': published_at,
                'thumbnails_default': thumbnails_default,
                'thumbnails_medium': thumbnails_medium,
                'thumbnails_high': thumbnails_high,
                'live_broadcast_content': live_broadcast_content,
                'publish_time': publish_time,
                'description': description,
            }
        )
    return {'videos': videos, 'next_page': data.get('nextPageToken')}


def main():
    query = 'dota '
    language = 'en'
    region_code = 'US'
    category_id = '22'
    topic_id = '/m/04rlf'

    videos = youtube_search_video(query, language=language, region_code=region_code,
                                  category_id=category_id, topic_id=topic_id)
    for video in videos:
        print(video)


if __name__ == '__main__':
    main()
