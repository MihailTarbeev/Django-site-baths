from django.urls import path, register_converter
from baths import views
from baths.converters import FourDigitYearConverter

register_converter(FourDigitYearConverter, "archive")


urlpatterns = [
    path('', views.index, name='home'),
    path('categories/<int:cat_id>/', views.categories, name='cat_int'),
    path('staff/', views.staff, name='staff'),
    path('categories/<slug:cat_slug>/', views.categories_by_slug, name='cat_slug'),
    path('archive/<archive:year>/', views.page_year, name='archive'),
]

