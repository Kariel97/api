from django.urls import path
from .views import listar, mostrar

urlpatterns = [
    path('listar/', listar, name="listar"),
    path('mostrar/' , mostrar, name="mostrar"),
]