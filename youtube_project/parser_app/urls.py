from django.urls import path


from parser_app.views.search_videos import parameters_selector_for_search_video
from parser_app.views.search_channels import parameters_selector_for_search_channels

urlpatterns = [
    path('videos/', parameters_selector_for_search_video, name='video'),
    path('channels/', parameters_selector_for_search_channels, name='channels'),
   ]
