from django.db import models

class Curso(models.Model):
    nombre = models.CharField(max_length=50)
    comision = models.IntegerField()

class Alumno(models.Model):
    nombre = models.CharField(max_length=50)
    dni = models.IntegerField()

class Profesor(models.Model):
    nombre = models.CharField(max_length=50)
    dni = models.IntegerField()