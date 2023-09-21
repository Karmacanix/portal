from django.urls import path

from cart.views import AddtoShoppingCartView, ShoppingCartCheckoutView

urlpatterns = [
    path("add/<int:item_id>/", AddtoShoppingCartView.as_view(), name='add_to_cart'),
    path("checkout/review/", ShoppingCartCheckoutView.as_view(), name='checkout_cart'),
]