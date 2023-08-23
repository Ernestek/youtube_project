from django.shortcuts import render

from parser_app.forms import ChoiceParamsVideoForm
from modules.search_video import youtube_search_video


def parameters_selector_for_search_video(request):
    if request.method == 'POST':
        form = ChoiceParamsVideoForm(request.POST)
        if form.is_valid():
            query = form.cleaned_data['query']
            language = form.cleaned_data['language']
            region = form.cleaned_data['region']
            category = form.cleaned_data['category']
            topic = form.cleaned_data['topic']
            video_caption = form.cleaned_data['video_caption']
            video_definition = form.cleaned_data['video_definition']
            video_embeddable = form.cleaned_data['video_embeddable']
            video_paid_product_placement = form.cleaned_data['video_paid_product_placement']
            video_syndicated = form.cleaned_data['video_syndicated']
            video_type = form.cleaned_data['video_type']
            video_license = form.cleaned_data['video_license']
            video_dimension = form.cleaned_data['video_dimension']
            date_from = str(form.cleaned_data['date_from'])  # + 'T00:00:00Z'
            date_to = str(form.cleaned_data['date_to'])  # + 'T00:00:00Z'

            page_token = None
            while True:
                youtube_data = youtube_search_video(query=query or None,
                                                    language=language or None,
                                                    region_code=region or None,
                                                    category_id=category or None,
                                                    topic_id=topic or None,
                                                    video_caption=video_caption,
                                                    video_definition=video_definition,
                                                    video_embeddable=video_embeddable,
                                                    video_paid_product_placement=video_paid_product_placement,
                                                    video_syndicated=video_syndicated,
                                                    video_type=video_type,
                                                    video_license=video_license,
                                                    video_dimension=video_dimension,
                                                    date_from=date_from or None,
                                                    date_to=date_to or None,
                                                    page_token=page_token)
                if youtube_data.get('next_page'):
                    page_token = youtube_data.get('next_page')
                else:
                    break
    else:
        form = ChoiceParamsVideoForm()

    return render(request, 'parser_app/search_video.html', {
        'form': form,
    })
