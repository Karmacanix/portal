from django.shortcuts import render
from django.forms import ModelForm, BaseModelFormSet, modelform_factory, Textarea
from django.views.generic import ListView
from django.views.generic.edit import UpdateView
from .models import Campaign, TargetAudience


# Create your views here.
class CampaignListView(ListView):
    model = Campaign
    context_object_name = "my_favorite_campaigns"


class CampaignDetailView(UpdateView):
    context_object_name = "topcampaign"
    queryset = Campaign.active_campaigns.all()
    success_url = '/campaign/list/'
    fields = '__all__'
