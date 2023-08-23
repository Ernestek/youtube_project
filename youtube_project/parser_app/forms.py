from django import forms

from common.enums import Languages, Region, Category, Topics


class ChoiceParamsVideoForm(forms.Form):
    query = forms.CharField(required=False)
    language = forms.ChoiceField(choices=Languages.choices, required=False)
    region = forms.ChoiceField(choices=Region.choices, required=False)
    category = forms.ChoiceField(choices=Category.choices, required=False)
    topic = forms.ChoiceField(choices=Topics.choices, required=False)


class ChoiceParamsChannelForm(forms.Form):
    query = forms.CharField(required=False)
    language = forms.ChoiceField(choices=Languages.choices, required=False)
    region = forms.ChoiceField(choices=Region.choices, required=False)
    topic = forms.ChoiceField(choices=Topics.choices, required=False)
