from django.urls import path, register_converter
from baths import views
from baths.converters import FourDigitYearConverter


urlpatterns = [
    path('', views.index, name='home'),
    path('about/', views.about, name='about'),
    path('add_bath/', views.add_bath, name='add_bath'),
    path('contact/', views.contact, name='contact'),
    path('login/', views.login, name='login'),
    path('bath/<int:bath_id>/', views.show_bath, name='bath'),
    path('categories/<int:cat_id>/', views.show_category, name='category'),

]

