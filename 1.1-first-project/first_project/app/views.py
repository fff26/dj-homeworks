from django.http import HttpResponse
from django.shortcuts import render, reverse

from datetime import datetime
import os


def home_view(request):
    template_name = 'app/home.html'
    # впишите правильные адреса страниц, используя
    # функцию `reverse`
    pages = {
        'Главная страница': reverse('home'),
        'Показать текущее время': 'current_time/',
        'Показать содержимое рабочей директории': 'workdir/'
    }
    
    # context и параметры render менять не нужно
    # подбробнее о них мы поговорим на следующих лекциях
    context = {
        'pages': pages
    }
    return render(request, template_name, context)


def time_view(request):
    current_time = str(datetime.now().time())[:8]
    msg = f'Текущее время: {current_time}'
    return HttpResponse(msg)


def workdir_view(request):
    current_dir = os.getcwd()
    files = os.listdir(current_dir)
    return HttpResponse(('\n'.join(files)))
