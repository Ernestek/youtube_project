from django.shortcuts import render

from parser_app.forms import ChoiceParamsVideoForm
from modules.search_video import youtube_search_video


def parameters_selector_for_search_video(request):
    youtube_data = {}

    if request.method == 'POST':
        form = ChoiceParamsVideoForm(request.POST)
        if form.is_valid():
            query = form.cleaned_data['query']
            language = form.cleaned_data['language']
            region = form.cleaned_data['region']
            category = form.cleaned_data['category']
            topic = form.cleaned_data['topic']

            page_token = None
            while True:
                youtube_data = youtube_search_video(query=query or None,
                                                    language=language or None,
                                                    region_code=region or None,
                                                    category_id=category or None,
                                                    topic_id=topic or None,
                                                    page_token=page_token)
                if youtube_data.get('next_page'):
                    page_token = youtube_data.get('next_page')
                else:
                    break
    else:
        form = ChoiceParamsVideoForm()

    return render(request, 'parser_app/search_video.html', {
        'form': form,
        # 'list_video': youtube_data.get('videos'),
    })


# def next_page_video(request, query: str, language=None, region_code=None, category_id=None, topic_id=None,
#                     count=10, page_token=None):
#     list_video = youtube_search_video(query=query or None,
#                                       language=language or None,
#                                       region_code=region_code or None,
#                                       category_id=category_id or None,
#                                       topic_id=topic_id or None)


def search_channel(request):
    ...
