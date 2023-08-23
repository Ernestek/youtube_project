import requests

from parser_app.models import Channels


def youtube_search_channels(query: str, language=None, region_code=None, topic_id=None,
                            count=50, page_token=None):
    base_url = "https://www.googleapis.com/youtube/v3/search"

    params = {
        'key': 'AIzaSyCRCu-0gmSjP2dTBh1NTXlO3vEWrLiKr_k',
        'q': query,
        'type': 'channel',
        'part': 'id,snippet',
        'maxResults': count,
        'relevanceLanguage': language,
        'regionCode': region_code,
        'topicId': topic_id,
        'pageToken': page_token
    }

    response = requests.get(base_url, params=params)
    data = response.json()

    channels = []
    for item in data.get('items', []):
        channel_id = item['id']['channelId']
        channel_title = item['snippet']['title']
        description = item['snippet']['description']
        # channels.append({
        #     'channel_id': channel_id,
        #     'channel_title': channel_title,
        #     'description': description,
        # })
        Channels.objects.get_or_create(
            channel_id=channel_id,
            defaults={
                'channel_title': channel_title,
                'description': description,
            }
        )
    return {'channels': channels, 'next_page': data.get('nextPageToken')}


def main():
    query = 'dota '
    language = 'en'
    region_code = 'US'
    topic_id = '/m/04rlf'

    channels = youtube_search_channels(query, language, region_code, topic_id)
    for channel in channels['channels']:
        print(channel)


if __name__ == '__main__':
    main()
