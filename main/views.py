from django.http import response
from django.shortcuts import render


def inicio(response):
    return render(response, 'main/inicio.html', {})

# def innovaciones(response):
#     return render(response, 'main/innovaciones.html', {})

# def contacto(response):
#     return render(response, 'main/contacto.html', {})