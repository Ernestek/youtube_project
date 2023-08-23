from django import forms

from common.enums import Languages, Region, Category, Topics, SafeSearch
from common.enums import (VideoType,
                          VideoSyndicated,
                          VideoCaption,
                          VideoLicense,
                          VideoDefinition,
                          VideoEmbeddable,
                          VideoDimension,
                          VideoPaidProductPlacement,)
from common.enums import ChannelType


class ChoiceParamsVideoForm(forms.Form):
    query = forms.CharField()
    language = forms.ChoiceField(choices=Languages.choices, required=False)
    region = forms.ChoiceField(choices=Region.choices, required=False)
    category = forms.ChoiceField(choices=Category.choices, required=False)
    topic = forms.ChoiceField(choices=Topics.choices, required=False)
    safe_search = forms.ChoiceField(choices=SafeSearch.choices, required=False)
    video_caption = forms.ChoiceField(choices=VideoCaption.choices, required=False)
    video_definition = forms.ChoiceField(choices=VideoDefinition.choices, required=False)
    video_embeddable = forms.ChoiceField(choices=VideoEmbeddable.choices, required=False)
    video_paid_product_placement = forms.ChoiceField(choices=VideoPaidProductPlacement.choices, required=False)
    video_syndicated = forms.ChoiceField(choices=VideoSyndicated.choices, required=False)
    video_type = forms.ChoiceField(choices=VideoType.choices, required=False)
    video_license = forms.ChoiceField(choices=VideoLicense.choices, required=False)
    video_dimension = forms.ChoiceField(choices=VideoDimension.choices, required=False)
    date_from = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}), required=False)
    date_to = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}), required=False)


class ChoiceParamsChannelForm(forms.Form):
    query = forms.CharField()
    language = forms.ChoiceField(choices=Languages.choices, required=False)
    region = forms.ChoiceField(choices=Region.choices, required=False)
    topic = forms.ChoiceField(choices=Topics.choices, required=False)
    channel_type = forms.ChoiceField(choices=ChannelType.choices, required=False)
    safe_search = forms.ChoiceField(choices=SafeSearch.choices, required=False)
    date_from = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}), required=False)
    date_to = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}), required=False)

