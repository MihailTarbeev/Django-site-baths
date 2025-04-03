from django.urls import path
from baths import views


urlpatterns = [
    path('', views.index),
    path('categories/<int:cat_id>/', views.categories),
]
