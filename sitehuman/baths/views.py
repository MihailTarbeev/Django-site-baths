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
    {'id': 1, 'name': 'Дом с ванной', 'check_in': '14:00', 'check_out': '12:00', 'description': 'В каждом домике: '
                                                                        'Мини кухня с холодильником, плиткой, чайником'
                                                                        ' и всей необходимой посудо'
                                                                        'Двуспальная кровать'
                                                                        'Туалет, душ и ванна с панорамным видом'
                                                                        'Система кондиционирования и отопления'
                                                                        'Небольшая терраса с видом на холмы'
                                                                        'В общем пользовании трех домов:'
                                                                        'зона барбекю'
                                                                        'лаунж с открытым костром'
                                                                        'Только двухместное размещение', 'open': False},
    {'id': 2, 'name': 'Барны', 'check_in': '14:00', 'check_out': '12:00', 'description': 'В каждом домике:'
                                                                        'Мини кухня с холодильником, плиткой, чайником'
                                                                        ' и всей необходимой посудой'
                                                                        'Двуспальная кровать на мансардном этаже с'
                                                                        ' видом на звездное небо'
                                                                        'Туалет и душ'
                                                                        'Система кондиционирования и отопления'
                                                                        'Небольшая терраса с видом на холмы'
                                                                        'В общем пользовании трех домов:'
                                                                        'зона барбекю'
                                                                        'лаунж с открытым костром'
                                                                        'Возможно трехместное размещение в Барнах '
                                                                        '(Дети до 6 лет размещаются бесплатно, без '
                                                                        'предоставления отдельного спального места)',
     'open': True},
    {'id': 3, 'name': 'Палатки', 'check_in': '14:00', 'check_out': '12:00', 'description': 'В каждой палатке:'
                                                'Удобная кровать и теплые одеяла (в палатках 1 и 2 две односпальные'
                                                ' кровати, в палатках 3, 4 и 5 двуспальные кровати)'
                                                'Простыни с подогревом'
                                                'Тепловая пушка'
                                                'Свет и розетки'
                                                'Вешалка'
                                                'Комплект полотенец'
                                                'Небольшая терраса'
                                                'На территории глэмпинга в общем пользовании:'
                                                'летняя кухня'
                                                '(микроволновка, холодильник, плита, термопот, гриль-барбекю, казан,'
                                                ' посуда и т.д.)'
                                                'лаунж с открытым костром'
                                                'душ (горячая, холодная вода), туалет'
                                                'открытый летний душ'
                                                'Возможно трехместное размещение (Дети до 6 лет размещаются бесплатно,'
                                                ' без предоставления отдельного спального места)', 'open': True}
]

cats_db = [
    {'id': 1, 'name': 'Русская'},
    {'id': 2, 'name': 'Турецкая'},
    {'id': 3, 'name': 'Египетская'},
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


def show_category(request, cat_id):
    return index(request)


def page_not_found(request, exception):
    return HttpResponseNotFound('<h1>Э! Вы кто такие! Я Вас не звал! Идите!</h1>')
