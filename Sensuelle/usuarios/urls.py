# usuarios/urls.py
from django.urls import path
from . import views

urlpatterns = [
    # Asegúrate de que la vista 'index' esté bien definida
    path('', views.index, name='index'),
]
