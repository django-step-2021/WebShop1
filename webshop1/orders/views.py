from django.shortcuts import render
from django.http import JsonResponse
from .models import Order


def ajax_cart(request):
    response = dict()
    uid = request.GET.get('uid')
    pid = request.GET.get('pid')

    Order.objects.create(
        title=f'Order-{pid}/{uid}',
        product_id=pid,
        user_id=uid,
        status='Ожидание подтверждения'
    )

    user_orders = Order.objects.filter(user_id=uid)
    cost = 0
    for order in user_orders:
        cost += order.product.price

    response['cost'] = cost
    response['count'] = len(user_orders)
    return JsonResponse(response)
