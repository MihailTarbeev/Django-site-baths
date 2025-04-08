from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect


# Create your views here.


def index(request):
    return HttpResponse('Hi!')


def categories(request, cat_id):
    print(request.GET)
    return HttpResponse(f'Категория {cat_id} <br>')


def categories_by_slug(request, cat_slug):
    return HttpResponse(f'<h1>Слаг: </h1> <p>{cat_slug}</p>')


def page_year(reqest, year):
    if year > 2025:
        return redirect(index, permanent=True)

    return HttpResponse(f'<h3>Запрашиваемый год:{year}')


def page_not_found(request, exception):
    return HttpResponseNotFound('<h1>Э! Вы кто такие! Я Вас не звал! Идите!</h1>')
