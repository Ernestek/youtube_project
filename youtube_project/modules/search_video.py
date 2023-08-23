import requests

from parser_app.models import Video


def youtube_search_video(query: str, language=None, region_code=None, category_id=None, topic_id=None,
                         count=50, page_token=None):
    base_url = "https://www.googleapis.com/youtube/v3/search"

    params = {
        'key': 'AIzaSyCRCu-0gmSjP2dTBh1NTXlO3vEWrLiKr_k',
        'q': query,
        'type': 'video',
        'part': 'id,snippet',
        'maxResults': count,
        'relevanceLanguage': language,
        'regionCode': region_code,
        'videoCategoryId': category_id,
        'topicId': topic_id,
        'pageToken': page_token
    }

    response = requests.get(base_url, params=params)
    data = response.json()

    videos = []
    for item in data.get('items', []):
        video_id = item['id']['videoId']
        channel_id = item['snippet']['channelId']
        channel_title = item['snippet']['channelTitle']
        title = item['snippet']['title']
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
            }
        )
    return {'videos': videos, 'next_page': data.get('nextPageToken')}


def main():
    query = 'dota '
    language = 'en'
    region_code = 'US'
    category_id = '22'
    topic_id = '/m/04rlf'

    videos = youtube_search_video(query, language, region_code, category_id, topic_id)
    for video in videos:
        print(video)


if __name__ == '__main__':
    main()
