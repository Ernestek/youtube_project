from django.shortcuts import render

from parser_app.forms import ChoiceParamsChannelForm
from modules.search_channels import youtube_search_channels


def parameters_selector_for_search_channels(request):
    if request.method == 'POST':
        form = ChoiceParamsChannelForm(request.POST)
        if form.is_valid():
            query = form.cleaned_data['query']
            language = form.cleaned_data['language']
            region = form.cleaned_data['region']
            topic = form.cleaned_data['topic']

            page_token = None

            while True:
                youtube_data = youtube_search_channels(query=query or None,
                                                       language=language or None,
                                                       region_code=region or None,
                                                       topic_id=topic or None,
                                                       page_token=page_token)
                if youtube_data.get('next_page'):
                    page_token = youtube_data.get('next_page')
                else:
                    break
    else:
        form = ChoiceParamsChannelForm()

    return render(request, 'parser_app/search_channels.html', {
        'form': form,
    })
