from djmoney.models.fields import MoneyField
from django.db import models
from mptt.models import MPTTModel, TreeForeignKey

class Catalog(MPTTModel):
    name = models.CharField(max_length=60, unique=True)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')

    class MPTTMeta:
        order_insertion_by = ['name']
        
    def get_absolute_url(self):
        return f"/catalog/{self.pk}/"
    
    def __str__(self):
        return self.name
    
    
class Service(models.Model):
    name = models.CharField(max_length=60, unique=True)
    category = TreeForeignKey(Catalog, on_delete=models.CASCADE, null=True, blank=True, related_name='catalog_item')
    cost = MoneyField(max_digits=14, decimal_places=2, default_currency='NZD', default=3.5)
    
    def get_absolute_url(self):
        return f"/service/{self.pk}/"
    
    def __str__(self):
        return self.name