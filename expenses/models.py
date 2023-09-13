from django.db import models
from django.contrib.auth import get_user_model

UserModel = get_user_model()


# Create your models here.
class ActiveExpenseManager(models.Manager):
    def get_active_expenses(self):
        return super().get_queryset().filter(active=True)
    
    
class Expense(models.Model):
    name = models.CharField(max_length=60)
    gl_code = models.CharField(max_length=120)
    desc = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()
    owner = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)
    active_expenses = ActiveExpenseManager()
    
    class Meta:
        ordering = ["-name"]

    def get_absolute_url(self):
        return f"/expense/{self.pk}/"
    
    def __str__(self):
        return self.name