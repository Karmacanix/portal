from django.db import models
from django.contrib.auth import get_user_model

from catalogue.models import Service

UserModel = get_user_model()
# need shoppingcart managers for active and maybe other statuses order or closed


class ActiveShoppingCart(models.Manager):
    def get_active_campaigns(self):
        return super().get_queryset().filter(active=True)


class ShoppingCart(models.Model):
    buyer = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    item = models.ForeignKey(Service, on_delete=models.CASCADE)
    quantity = models.PositiveSmallIntegerField(default=1, blank=False)
    added = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)
    active_shoppingcart = ActiveShoppingCart()
    
    class Meta:
        unique_together = ["buyer", "item"]

    def get_absolute_url(self):
        return f"/cart/{self.pk}/"
    
    def __str__(self):
        return self.item.name


# Create your models here.
class ShoppingCartItem(models.Model):
    cart = models.ForeignKey(ShoppingCart, on_delete=models.CASCADE)
    added = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    def get_absolute_url(self):
        return f"/cart/item/{self.pk}/"
    
    def __str__(self):
        return self.cart


class Checkout(models.Model):
    pass


class Address(models.Model):
    ADD_CHOICES = [
        ("SHIP","Shipping Address"),
        ("BILL","Billing Address"),
    ]
    type = models.CharField(
        max_length = 4,
        choices=ADD_CHOICES,
        default="SHIP",
        help_text="Select address type:",
    )
    buyer = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    add1 = models.CharField(max_length=50)
    add2 = models.CharField(max_length=50)
    city = models.CharField(max_length=20)
    region = models.CharField(max_length=20)
    postcode = models.CharField(max_length=6)
    

class Purchase(models.Model):
    ADD_CARD = [
        ("VISA","VISA"),
        ("MASC","Mastercard"),
    ]
    card_type = models.CharField(
        max_length = 4,
        choices=ADD_CARD,
        default="VISA",
        help_text="Select address type:",
    )
    buyer = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    card_number = models.CharField(max_length=50)