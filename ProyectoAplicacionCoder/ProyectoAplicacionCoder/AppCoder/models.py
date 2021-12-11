from django.db import models

# Create your models here.
class Curso(models.Model):

    nombre = models.CharField(max_length=40)
    comision = models.IntegerField()
    esNoche = models.BooleanField(null=True)

    def __str__(self):

        return f"CURSO: {self.nombre} CAMADA: {self.comision}"

class  Jugador(models.Model):

    apellido = models.CharField(max_length=40)
    numero = models.IntegerField()
    esBueno = models.BooleanField()

    def __str__(self):

        return f"APELLIDO: {self.apellido}"

class Equipo(models.Model):
    nombre = models.CharField(max_length=40)
    ciudad = models.CharField(max_length=40)

    def __str__(self):

        return f"Equipo: {self.nombre} Ciudad: {self.ciudad}"

class Estadio(models.Model):

    direccion = models.CharField(max_length=40)
    anioFund = models.IntegerField()

    def __str__(self):

        return f"Direccion: {self.direccion} Año Fundacion: {self.anioFund}"
