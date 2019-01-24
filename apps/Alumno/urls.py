from django.conf.urls import url
from apps.Alumno.views import crearAlumno, editarAlumno, listarAlumnos, eliminarAlumno

urlpatterns = [
    url(r'^home$', listarAlumnos.as_view(), name='listar'),
    url(r'^eliminarAlumno/(?P<pk>\d+)$', eliminarAlumno.as_view(), name='eliminar'),
    url(r'^editarAlumno/(?P<pk>\d+)$', editarAlumno.as_view(), name='editar'),
    url(r'^crearAlumno$', crearAlumno.as_view(), name = 'crear'),
]
