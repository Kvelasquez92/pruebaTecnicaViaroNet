from django.db import models

# Create your models here.

class Profesor(models.Model):
    nombre = models.CharField(max_length=100, null=False, blank=False)
    apellidos = models.CharField(max_length=100, null=False, blank=False)
    genero = models.CharField(max_length=1, null=False, blank=False)
