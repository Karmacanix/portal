from typing import Any
from django import forms
from django.db import models 
from django.db.models import CharField, DecimalField, Value
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, FormView

from cart.models import ShoppingCart, Address, Purchase
from catalogue.models import Service
from cart.forms import AddressForm, PurchaseForm

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


class ShoppingCartCheckoutView(ListView):
    model= ShoppingCart
    template_name = "cart/checkout.html"
    fields = ['buyer', "item", "quantity"]
    
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        buyer = self.request.user
        t = 0
        c = ShoppingCart.active_shoppingcart.filter(buyer = buyer)
        cart = c.annotate(subtotal=Value('0', output_field=DecimalField(max_digits=14, decimal_places=2)))
        for i in cart:
            i.subtotal=i.quantity*i.item.cost
            t = t+i.subtotal
            print(i.subtotal, t)
        
        context['cart'] = cart
        context['total'] = t
        return context


class AddressCheckout(FormView):
    queryset = None
    template_name = "cart/shipping.html"
    fileds = ['__all__']
    form_class = AddressForm
    
    def get_queryset(self):
        buyer = self.request.user
        return super().get_queryset(Address.objects.get(buyer=buyer))
    
    def get_initial(self) -> dict[str, Any]:
        buyer = self.request.user
        if self.queryset == None:
            form = forms.Form(initial=buyer)
        return super().get_initial()


class PurchaseCheckout(FormView):
    queryset = None
    template_name = "cart/purchase.html"
    fileds = ['__all__']
    form_class = PurchaseForm
    
    def get_queryset(self):
        buyer = self.request.user
        return super().get_queryset(Purchase.objects.get(buyer=buyer))
    
    def get_initial(self) -> dict[str, Any]:
        buyer = self.request.user
        if self.queryset == None:
            form = PurchaseForm(initial=buyer)
        return super().get_initial()