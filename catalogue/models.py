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
    SERVICE_TYPE_CHOICES = [
        ("S","Service"),
        ("P","Product"),
        ("I","Report Incident"),
    ]
    service_type = models.CharField(
        max_length = 1,
        choices=SERVICE_TYPE_CHOICES,
        default="S",
        help_text="Select service type:",
    )
   #costcentre n/ or 4 digit code
    #additional information on submit
    # notes
    APPROVAL_TYPE_CHOICES = [
        ("MAN","Manager"),
        ("NON","No approval required"),
        ("BUS","Business Owner"),
        ("CST","Cost Centre Owner"),
    ]
    approval_type = models.CharField(
        max_length = 3,
        choices=APPROVAL_TYPE_CHOICES,
        default="MAN",
        help_text="Select approval type:",
    )
    # cost_centre = models.PositiveSmallIntegerField(default=0, help_text="Expense account to charge this service to")
    # notes = models.TextField(blank=True, help_text="Additional information required to get access to this service.")
    
    def get_absolute_url(self):
        return f"/service/{self.pk}/"
    
    def __str__(self):
        return self.name