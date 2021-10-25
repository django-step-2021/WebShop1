from django.urls import path
from .views import ajax_cart, index, ajax_cart_display

urlpatterns = [
    path('ajax_cart', ajax_cart),
    path('', index),
    path('ajax_cart_display', ajax_cart_display),
]
