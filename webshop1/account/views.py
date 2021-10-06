from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse


def register(request):
    if request.method == 'GET':
        return render(request, 'account/register.html', context={
            'page_name': 'Регистрация',
            'page_app': 'account',
            'page_view': 'register',
        })
    elif request.method == 'POST':
        login_x = request.POST.get('login')
        pass1_x = request.POST.get('pass1')
        pass2_x = request.POST.get('pass2')
        email_x = request.POST.get('email')

    # 1 - Валидация данных на стороне сервера ...

    # 2 - Сохранение пользователя в базе данных ...
    user = User.objects.create_user(login_x, email_x, pass1_x)
    if user is None:
        mess = 'В регистрации отказано!'
        color = 'red'
    else:
        user.save()
        mess = 'Регистрация успешно завершена!'
        color = 'green'

    # 3 - Вывод отчета ...
    return render(request, 'account/report.html', context={
        'page_name': 'Отчет о регистрации',
        'page_app': 'account',
        'page_view': 'report',
        'mess': mess,
        'color': color,
    })
