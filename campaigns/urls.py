
from django.urls import include, path
from .models import Campaign, TargetAudience
from .views import CampaignListView, CampaignDetailView

urlpatterns = [
    path("list/", CampaignListView.as_view(), name='campaign_list'),
    path("<int:pk>/", CampaignDetailView.as_view(), name='campaign_details'),
]
