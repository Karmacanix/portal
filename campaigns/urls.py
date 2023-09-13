
from django.urls import include, path
from .models import Campaign, TargetAudience
from .views import CampaignListView, CampaignDetailView, CampaignUpdateView

urlpatterns = [
    path("list/", CampaignListView.as_view(), name='campaign_list'),    
    path("detail/<int:pk>/", CampaignDetailView.as_view(), name='campaign_details'),
    path("update/<int:pk>/", CampaignUpdateView.as_view(), name='campaign_update'),
]
