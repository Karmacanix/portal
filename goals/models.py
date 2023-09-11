from django.db import models
from django.contrib.auth import get_user_model

UserModel = get_user_model()


# Create your models here.
class ActiveGoalManager(models.Manager):
    def get_active_goals(self):
        return super().get_queryset().filter(active=True)
    
    
class Goal(models.Model):
    specific = models.CharField(max_length=60)
    success_measure = models.CharField(max_length=120)
    justification = models.TextField()
    target_date = models.CharField(max_length=120)
    business_owner = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)
    active_goals = ActiveGoalManager()
    
    class Meta:
        ordering = ["-specific"]

    def get_absolute_url(self):
        return f"/goal/{self.pk}/"
    
    def __str__(self):
        return self.specific