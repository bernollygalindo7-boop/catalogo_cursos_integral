from django.shortcuts import render, redirect, get_object_or_404
from .models import Curso

def lista_cursos(request):
    cursos = Curso.objects.all()
    return render(request, 'cursos/lista.html', {'cursos': cursos})

def crear_curso(request):
    if request.method == 'POST':
        Curso.objects.create(
            nombre=request.POST['nombre'],
            duracion=request.POST['duracion'],
            plataforma=request.POST['plataforma'],
            dificultad=request.POST['dificultad'],
        )
        return redirect('lista_cursos')
    return render(request, 'cursos/crear.html')

def editar_curso(request, id):
    curso = get_object_or_404(Curso, id=id)
    if request.method == 'POST':
        curso.nombre = request.POST['nombre']
        curso.duracion = request.POST['duracion']
        curso.plataforma = request.POST['plataforma']
        curso.dificultad = request.POST['dificultad']
        curso.save()
        return redirect('lista_cursos')
    return render(request, 'cursos/editar.html', {'curso': curso})

def eliminar_curso(request, id):
    curso = get_object_or_404(Curso, id=id)
    curso.delete()
    return redirect('lista_cursos')
