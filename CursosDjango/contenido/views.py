from django.shortcuts import render
from django.http import HttpResponse


def inicio(request):
    return render(request, 'inicio.html')

def cursos(request):
    lista_cursos = ['Programación', 'Base de Datos', 'Desarrollo Web']
    return render(request, 'cursos.html', {'cursos': lista_cursos})

def contacto(request):
    return render(request, 'contacto.html')


def index(request):
    return HttpResponse("Hola desde la app cursos.")



