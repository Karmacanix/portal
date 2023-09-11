from django.db import models
from django.contrib.auth import get_user_model

UserModel = get_user_model()


# Create your models here.
class ActiveCampaignManager(models.Manager):
    def get_active_campaigns(self):
        return super().get_queryset().filter(active=True)
    

class Campaign(models.Model):
    name = models.CharField(max_length=60)
    target_date = models.CharField(max_length=120)
    sponsor = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    # fk m2m TargetAudience
    # fk m2m Goals
    # desc-justifications
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)
    active_campaigns = ActiveCampaignManager()

    class Meta:
        ordering = ["-name"]

    def get_absolute_url(self):
        return f"/campaign/{self.pk}/"
    
    def __str__(self):
        return self.name


# wrap all the people needs into a target audience
class TargetAudience(models.Model):
    # generation options
    # generations
    # need
    pass




