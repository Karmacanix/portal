from django.urls import path

from cart.views import AddtoShoppingCartView, ShoppingCartCheckoutView, AddressCheckout

urlpatterns = [
    path("add/<int:item_id>/", AddtoShoppingCartView.as_view(), name='add_to_cart'),
    path("checkout/review/", ShoppingCartCheckoutView.as_view(), name='checkout_cart'),
    path("checkout/address/", AddressCheckout.as_view(), name='shipping_address'),
    path("checkout/purchase/", AddressCheckout.as_view(), name='purchase_order'),
]