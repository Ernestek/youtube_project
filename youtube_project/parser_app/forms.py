from django import forms
from django.utils import timezone

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


class ChoiceDate(forms.Form):
    date_from = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}), required=False)
    date_to = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}), required=False)

    def clean(self):
        cleaned_data = super().clean()
        date_from = cleaned_data.get('date_from')
        date_to = cleaned_data.get('date_to')
        today = timezone.now().date()

        if date_from and date_to and date_from > date_to:
            raise forms.ValidationError("Date From cannot be greater than Date To")
        if date_from and date_from > today:
            raise forms.ValidationError("Date From cannot be in the future")
        if date_to and date_to > today:
            raise forms.ValidationError("Date To cannot be in the future")


class ChoiceParamsVideoForm(ChoiceDate):
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
    # date_from = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}), required=False)
    # date_to = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}), required=False)


class ChoiceParamsChannelForm(ChoiceDate):
    query = forms.CharField()
    language = forms.ChoiceField(choices=Languages.choices, required=False)
    region = forms.ChoiceField(choices=Region.choices, required=False)
    topic = forms.ChoiceField(choices=Topics.choices, required=False)
    channel_type = forms.ChoiceField(choices=ChannelType.choices, required=False)
    safe_search = forms.ChoiceField(choices=SafeSearch.choices, required=False)
    # date_from = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}), required=False)
    # date_to = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}), required=False)

