from django.urls import path
from . import views

urlpatterns = [
    #HOME
    path("inicio",views.inicio),

    #CURSOS
    path("curso_alta", views.curso_formulario),
    path("cursos", views.cursos_ver,),
    path("curso_buscar",views.curso_buscar),
    path("curso_resultado",views.curso_resultado),

    #PROFESORES
    path("profesores",views.profesores_ver),
    path("profesor_alta",views.profesor_formulario),
    path("profesor_buscar",views.profesor_buscar),
    path("profesor_resultado",views.profesor_resultado),

    #ALUMNOS
    path("alumnos",views.alumnos_ver),
    path("alumno_alta",views.alumno_formulario),
    path("alumno_buscar",views.alumno_buscar),
    path("alumno_resultado", views.alumno_resultado),
]
