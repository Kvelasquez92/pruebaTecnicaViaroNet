from django.db import models
from apps.Alumno.models import Alumno
from apps.Grado.models import Grado


# Create your models here.

class AlumnoGrado(models.Model):
    alumnoId = models.ForeignKey(Alumno, null=False, blank=False, on_delete=models.CASCADE)
    gradoId = models.ForeignKey(Grado, null=False, blank=False, on_delete=models.CASCADE)
    seccion = models.CharField(max_length=1, null=False, blank=False)
