from django.http import HttpResponse, HttpResponseNotFound, Http404, HttpResponseRedirect, HttpResponsePermanentRedirect
from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from django.urls import reverse


# Create your views here.


def index(request):
    # t = render_to_string('baths/index.html')
    # return HttpResponse(t)
    return render(request, 'baths/index.html')


def staff(request):
    return render(request, 'baths/staff.html')


def categories(request, cat_id):
    print(request.GET)
    return HttpResponse(f'Категория {cat_id} <br>')


def categories_by_slug(request, cat_slug):
    return HttpResponse(f'<h1>Слаг: </h1> <p>{cat_slug}</p>')


def page_year(request, year):
    if year > 2025:
        url = reverse('cat_slug', args=('music',))
        return HttpResponsePermanentRedirect('/')

    return HttpResponse(f'<h3>Запрашиваемый год:{year}')


def page_not_found(request, exception):
    return HttpResponseNotFound('<h1>Э! Вы кто такие! Я Вас не звал! Идите!</h1>')
