from django import forms
from django.core.exceptions import ValidationError
from django.forms import BaseModelFormSet
from django.forms import modelformset_factory
from django.forms import inlineformset_factory



class TargetAudienceFormSet(BaseModelFormSet):
    def clean(self):
        super().clean()

        for form in self.forms:
            name = form.cleaned_data["name"].upper()
            form.cleaned_data["name"] = name
            # update the instance value.
            form.instance.name = name


class ChildCampaignFormSet(BaseModelFormSet):
    def clean(self):
        super().clean()

        for form in self.forms:
            name = form.cleaned_data["name"].upper()
            form.cleaned_data["name"] = name
            # update the instance value.
            form.instance.name = name