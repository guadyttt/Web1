from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
#Import App1
from App1.models import Curso,Profesor, Alumno
from App1.forms import Curso_fomulario, Profesor_formulario, Alumno_formulario

# Create your views here.

def inicio(request):
    return render(request, "inicio.html")

#CURSOS

def curso_formulario(request):
    if request.method =="POST":
        mi_formulario = Curso_fomulario(request.POST)
        if mi_formulario.is_valid():
            datos = mi_formulario.cleaned_data
            curso = Curso(nombre=request.POST["nombre"], comision=request.POST["comision"])
            curso.save()
            return render(request,"curso_formulario.html")
    return render(request,"curso_formulario.html")


def cursos_ver(request):
    cursos = Curso.objects.all()
    dicc = {"cursos": cursos}
    plantilla = loader.get_template("cursos.html")
    documento = plantilla.render(dicc)
    return HttpResponse(documento)


def curso_buscar(request):
    return render(request, "curso_buscar.html")


def curso_resultado(request):

    if request.GET["nombre"]:
        nombre = request.GET["nombre"]
        cursos = Curso.objects.filter(nombre__icontains= nombre)
        return render(request,"curso_resultado.html",{"cursos":cursos})
    else:
        return render(request,"curso_buscar_error.html")

def curso_eliminar(request, id):
    curso = Curso.objects.get(id=id)
    curso.delete()
    cursos = Curso.objects.all()
    return render (request, "curso_eliminado.html", {"cursos":cursos})

#PROFESORES

def profesor_formulario(request):
    if request.method =="POST":
        mi_formulario = Profesor_formulario(request.POST)
        if mi_formulario.is_valid():
            datos = mi_formulario.cleaned_data
            profesor = Profesor(nombre=request.POST["nombre"], dni=request.POST["dni"])
            profesor.save()
            return render(request, "profesor_formulario.html")
    return render(request, "profesor_formulario.html")


def profesores_ver(request):
    profesores = Profesor.objects.all()
    dicc = {"profesores":profesores}
    plantilla = loader.get_template("profesores.html")
    documento = plantilla.render(dicc)
    return HttpResponse(documento)


def profesor_buscar(request):
    return render(request,"profesor_buscar.html")


def profesor_resultado(request):
    if request.GET["nombre"]:
        nombre = request.GET["nombre"]
        profesores = Profesor.objects.filter(nombre__icontains= nombre)
        return render(request,"profesor_resultado.html",{"profesores":profesores})
    else:
        return render(request,"profesor_buscar_error.html")


#ALUMNOS

def alumno_formulario(request):
    if request.method == "POST":
        mi_formulario = Alumno_formulario(request.POST)
        if mi_formulario.is_valid():
            datos = mi_formulario.cleaned_data
            alumno = Alumno(nombre=request.POST["nombre"], dni=request.POST["dni"])
            alumno.save()
            return render(request , "alumno_formulario.html")
    return render(request , "alumno_formulario.html")


def alumnos_ver(request):
    alumnos = Alumno.objects.all()
    dicc = {"alumnos":alumnos}
    plantilla = loader.get_template("alumnos.html")
    documento = plantilla.render(dicc)
    return HttpResponse(documento)


def alumno_buscar(request):
    return render(request, "alumno_buscar.html")


def alumno_resultado(request):
    if request.GET["nombre"]:    
        nombre = request.GET["nombre"]
        alumnos = Alumno.objects.filter(nombre__icontains= nombre)
        return render(request,"alumno_resultado.html",{"alumnos":alumnos})
    else:
        return render(request,"alumno_buscar_error.html")

