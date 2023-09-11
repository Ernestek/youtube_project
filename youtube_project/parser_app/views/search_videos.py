from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.shortcuts import render

from parser_app.forms import ChoiceParamsVideoForm
from modules.search_video import youtube_search_video
from parser_app.models import Video


@login_required
def parameters_selector_for_search_video(request):
    form = None
    if request.method == 'POST':
        if not request.user.user_tariff.is_search_limit_exceeded():
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
                                                        user=request.user,
                                                        date_from=date_from or None,
                                                        date_to=date_to or None,
                                                        page_token=page_token)
                    if youtube_data.get('next_page'):
                        page_token = youtube_data.get('next_page')
                    else:
                        break
    else:
        form = ChoiceParamsVideoForm()

    form = form or ChoiceParamsVideoForm()
    count_search_request = request.user.user_tariff.remaining_searches
    page_number = request.GET.get('page')  # Получение номера страницы из URL параметра
    per_page = int(request.GET.get('per_page', 10))  # Получение количества на странице, по умолчанию 10
    videos = get_video_list(page_number, per_page, user=request.user)

    return render(request, 'parser_app/search_video.html', {
        'form': form,
        'videos': videos,
        'count_search_request': count_search_request,
    })


def get_video_list(page_number, per_page, user):
    videos = Video.objects.filter(user=user).order_by('id')
    paginator = Paginator(videos, per_page)
    page = paginator.get_page(page_number)
    return page
