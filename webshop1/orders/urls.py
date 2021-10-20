from django.urls import path
from .views import ajax_cart, index

urlpatterns = [
    path('ajax_cart', ajax_cart),
    path('', index),
]
