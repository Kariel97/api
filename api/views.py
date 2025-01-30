from django.shortcuts import render
import requests
from datetime import datetime

def listar(request):
    url = "https://django-etl-challenge.vercel.app/api/generate"
    resp = requests.get(url)
    return resp.json()


def filtrar_color(request):

    datos = listar(request)
    # Filtrar y ordenar los datos por color y fecha (de más reciente a más antiguo)
    datos_filtrados = {}
    for item in datos:
        color = item['color']
        if color not in datos_filtrados:
            datos_filtrados[color] = []
        datos_filtrados[color].append(item)
    
    # Ordenar los items dentro de cada color por fecha
    for color in datos_filtrados:
        datos_filtrados[color].sort(key=lambda x: datetime.strptime(x['fecha'], '%Y-%m-%d'), reverse=True)

    return datos_filtrados

def mostrar(request):
    datos = filtrar_color(request)
    return render(request, 'api/mostrar.html', {'datos': datos})
