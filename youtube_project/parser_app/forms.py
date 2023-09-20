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
    date_from = forms.DateField(widget=forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}), required=False)
    date_to = forms.DateField(widget=forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}), required=False)

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
    query = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Search', 'class': 'form-control'}))
    language = forms.ChoiceField(choices=Languages.choices, required=False, widget=forms.Select(attrs={'class': 'form-select'}))  # widget=forms.TextInput(attrs={'list': 'my_field_choices'}),
    region = forms.ChoiceField(choices=Region.choices, required=False, widget=forms.Select(attrs={'class': 'form-select'}))
    category = forms.ChoiceField(choices=Category.choices, required=False, widget=forms.Select(attrs={'class': 'form-select'}))
    topic = forms.ChoiceField(choices=Topics.choices, required=False, widget=forms.Select(attrs={'class': 'form-select'}))
    safe_search = forms.ChoiceField(choices=SafeSearch.choices, required=False, widget=forms.Select(attrs={'class': 'form-select'}))
    video_caption = forms.ChoiceField(choices=VideoCaption.choices, required=False, widget=forms.Select(attrs={'class': 'form-select'}))
    video_definition = forms.ChoiceField(choices=VideoDefinition.choices, required=False, widget=forms.Select(attrs={'class': 'form-select'}))
    video_embeddable = forms.ChoiceField(choices=VideoEmbeddable.choices, required=False, widget=forms.Select(attrs={'class': 'form-select'}))
    video_paid_product_placement = forms.ChoiceField(choices=VideoPaidProductPlacement.choices, required=False, widget=forms.Select(attrs={'class': 'form-select'}))
    video_syndicated = forms.ChoiceField(choices=VideoSyndicated.choices, required=False, widget=forms.Select(attrs={'class': 'form-select'}))
    video_type = forms.ChoiceField(choices=VideoType.choices, required=False, widget=forms.Select(attrs={'class': 'form-select'}))
    video_license = forms.ChoiceField(choices=VideoLicense.choices, required=False, widget=forms.Select(attrs={'class': 'form-select'}))
    video_dimension = forms.ChoiceField(choices=VideoDimension.choices, required=False, widget=forms.Select(attrs={'class': 'form-select'}))


class ChoiceParamsChannelForm(ChoiceDate):
    query = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Search', 'class': 'form-control'}))
    language = forms.ChoiceField(choices=Languages.choices, required=False,)
    region = forms.ChoiceField(choices=Region.choices, required=False, widget=forms.Select(attrs={'class': 'form-select'}))
    topic = forms.ChoiceField(choices=Topics.choices, required=False, widget=forms.Select(attrs={'class': 'form-select'}))
    channel_type = forms.ChoiceField(choices=ChannelType.choices, required=False, widget=forms.Select(attrs={'class': 'form-select'}))
    safe_search = forms.ChoiceField(choices=SafeSearch.choices, required=False, widget=forms.Select(attrs={'class': 'form-select'}))
