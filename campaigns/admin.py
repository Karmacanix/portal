from django.contrib import admin
from .models import Campaign, TargetAudience
# Register your models here.


class TargetAudienceInline(admin.TabularInline):
    model = TargetAudience


class ChildCampaignAudienceInline(admin.TabularInline):
    model = Campaign


class CampaignAdmin(admin.ModelAdmin):
    inlines = [
        TargetAudienceInline,
        ChildCampaignAudienceInline,
    ]


admin.site.register(Campaign, CampaignAdmin)
