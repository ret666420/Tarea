from django.shortcuts import render
from .models import Curso

def index(request):
    cursos = Curso.objects.all()
    return render(request, 'cursos.html', {'cursos': cursos})
