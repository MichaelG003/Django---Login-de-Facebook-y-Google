# productos/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    # Agrega otras rutas si es necesario
]
