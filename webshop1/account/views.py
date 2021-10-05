from django.shortcuts import render


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

    # 1 - Валидация данных ...

    # 2 - Сохранение пользователя в базе данных ...

    # 3 - Вывод отчета ...
    return render(request, 'account/report.html', context={
        'page_name': 'Отчет о регистрации',
        'page_app': 'account',
        'page_view': 'report',
    })
