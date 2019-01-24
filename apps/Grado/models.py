from django.db import models
from apps.Profesor.models import Profesor

# Create your models here.

class Grado(models.Model):
    nombre = models.CharField(max_length=100, null=False, blank=False)
    profesorId = models.ForeignKey(Profesor, null=False, blank=False, on_delete=models.CASCADE)
