from typing import Any
from django.shortcuts import render
from django.forms import ModelForm, BaseModelFormSet, modelform_factory, Textarea
from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView
from .models import Campaign, TargetAudience


# Create your views here.
class CampaignListView(ListView):
    model = Campaign
    context_object_name = "campaign_list"
    template_name = "campaign_list.html"
    
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['target'] = super().get_context_data(**kwargs)
        return context


class CampaignUpdateView(UpdateView):
    context_object_name = "current_campaign"
    queryset = Campaign.active_campaigns.all()
    success_url = '/campaign/list/'
    fields = '__all__'
    template_name = "campaigns/campaign_form.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['target'] = TargetAudience.objects.filter(pk=self.object.pk)
        return context


class CampaignDetailView(DetailView):
    context_object_name = "current_campaign"
    model = Campaign
    fields = '__all__'
    template_name = "campaigns/campaign_detail.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['target'] = TargetAudience.objects.filter(campaign_id=self.object.id)
        print(context['target'])
        return context