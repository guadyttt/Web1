from django.db import models

class Curso(models.Model):
    nombre = models.CharField(max_length=50)
    comision = models.IntegerField()
    def __str__(self):
        return f"{self.nombre}, {self.comision}"

class Alumno(models.Model):
    nombre = models.CharField(max_length=50)
    dni = models.IntegerField()
    def __str__(self):
        return f"{self.nombre}, {self.dni}"

class Profesor(models.Model):
    nombre = models.CharField(max_length=50)
    dni = models.IntegerField()
    def __str__(self):
        return f"{self.nombre}, {self.dni}"