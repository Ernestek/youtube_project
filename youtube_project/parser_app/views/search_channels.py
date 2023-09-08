from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.paginator import Paginator
from django.shortcuts import render

from parser_app.forms import ChoiceParamsChannelForm
from modules.search_channels import youtube_search_channels
from parser_app.models import Channels, UserTariff


@login_required
def parameters_selector_for_search_channels(request):
    form = None
    if request.method == 'POST':
        # user = User.objects.select_related('user_tariff').get(user_name=request.user.username)
        if not request.user.user_tariff.is_search_limit_exceeded():

            form = ChoiceParamsChannelForm(request.POST)
            if form.is_valid():
                query = form.cleaned_data['query']
                language = form.cleaned_data['language']
                region = form.cleaned_data['region']
                topic = form.cleaned_data['topic']
                channel_type = form.cleaned_data['channel_type']
                safe_search = form.cleaned_data['safe_search']
                date_from = str(form.cleaned_data['date_from'])  # + 'T00:00:00Z'
                date_to = str(form.cleaned_data['date_to'])  # + 'T00:00:00Z'

                page_token = None

                while True:
                    youtube_data = youtube_search_channels(query=query or None,
                                                           language=language or None,
                                                           region_code=region or None,
                                                           topic_id=topic or None,
                                                           channel_type=channel_type,
                                                           safe_search=safe_search,
                                                           date_from=date_from or None,
                                                           date_to=date_to or None,
                                                           page_token=page_token)
                    if youtube_data.get('next_page'):
                        page_token = youtube_data.get('next_page')
                    else:
                        break
                request.user.user_tariff.decrement_search_limit()

    form = form or ChoiceParamsChannelForm()
    count_search_request = request.user.user_tariff.remaining_searches
    page_number = request.GET.get('page')  # Получение номера страницы из URL параметра
    per_page = int(request.GET.get('per_page', 10))  # Получение количества на странице, по умолчанию 10
    channels = get_channel_list(page_number, per_page)

    return render(request, 'parser_app/search_channels.html', {
        'form': form,
        'channels': channels,
        'count_search_request': count_search_request,
    })


def get_channel_list(page_number, per_page):
    channels = Channels.objects.order_by('id').all()
    paginator = Paginator(channels, per_page)
    page = paginator.get_page(page_number)
    return page


# def check_user_tariff