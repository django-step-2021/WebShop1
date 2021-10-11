from django.urls import path
from .views import register, entry, sign_out

urlpatterns = [
    path('register', register),
    path('entry', entry),
    path('logout', sign_out),
]
