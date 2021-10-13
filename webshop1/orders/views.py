from django.shortcuts import render
from django.http import JsonResponse
from .models import Order


def ajax_cart(request):
    response = dict()
    response['test'] = 'Ajax - work!'
    return JsonResponse(response)