from django.http import HttpResponse, HttpResponseNotFound, Http404, HttpResponseRedirect, HttpResponsePermanentRedirect
from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from django.urls import reverse

menu = [
    {'title': 'Главная', 'url_name': 'home'},
    {'title': 'О сайте', 'url_name': 'about'},
    {'title': 'Добавить баню', 'url_name': 'add_bath'},
    {'title': 'Обратная связь', 'url_name': 'contact'},
    {'title': 'Войти', 'url_name': 'login'},
]

baths = [
    {'id': 1, 'name': 'Банька Парилка', 'capacity': 20, 'open': False},
    {'id': 2, 'name': 'Банька от Аньки', 'capacity': 100, 'open': True},
    {'id': 3, 'name': 'Русская баня', 'capacity': 50, 'open': True}
]


def index(request):
    # t = render_to_string('baths/index.html')
    # return HttpResponse(t)
    data = {'title': 'Главная', 'menu': menu, 'baths': baths}
    return render(request, 'baths/index.html', context=data)


def show_bath(request, bath_id):
    return HttpResponse(f'<p>Банька с номером {bath_id}</p>')


def about(request):
    data = {'title': 'О сайте', 'menu': menu}
    return render(request, 'baths/about.html', context=data)


def add_bath(request):
    return HttpResponse(f'<p>Добавление баньки</p>')


def contact(request):
    return HttpResponse(f'<p>Обратная связь</p>')


def login(request):
    return HttpResponse(f'<p>Авторизация</p>')


def page_not_found(request, exception):
    return HttpResponseNotFound('<h1>Э! Вы кто такие! Я Вас не звал! Идите!</h1>')
