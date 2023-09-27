from django import forms

from cart.models import Address, Purchase

 
class AddressForm(forms.ModelForm):
    
    class Meta:
        model = Address
        fields = ("buyer", "add1", "add2", "type", "city", "region", "postcode")


class PurchaseForm(forms.ModelForm):
    
    class Meta:
        model = Purchase
        fields = ("buyer", "card_type", "card_number")