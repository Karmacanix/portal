from typing import Any
from django import forms 
from django.views.generic.edit import CreateView, UpdateView

from cart.models import ShoppingCart, ShoppingCartItem
from catalogue.models import Service

# Create your views here.

class AddtoShoppingCartView(UpdateView):
    model = ShoppingCart
    template_name = "cart/cart.html"
    fields = ['buyer', 'item', 'quantity']
    success_url = '/catalog/list/'
    
    def get_object(self, queryset=None):
        item = Service.objects.get(id=self.kwargs.get("item_id"))
        buyer = self.request.user
        obj, created = ShoppingCart.objects.get_or_create(buyer=buyer, item=item)
        print("Object. Item:", item, " User:", buyer, " Shopping Cart:", obj, " Created:", created)
        return obj
        
    def get_context_data(self, **kwargs) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        item = Service.objects.get(id=self.kwargs.get("item_id"))
        print("Context. Item:", item, " Catalog:", item.category.name)
        context["catalog_id"] = item.category.id
        return context
    
    def get_form(self, form_class=None):
        form = super().get_form( form_class)
        form.fields['buyer'].widget = forms.HiddenInput()
        form.fields['item'].widget = forms.HiddenInput()
        return form


class ShoppingCartCheckoutView(CreateView):
    pass

