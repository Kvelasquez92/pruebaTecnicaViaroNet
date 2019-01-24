from django.conf.urls import url
from apps.AlumnoGrado.views import crearAlumnoGrado, editarAlumnoGrado, listarAlumnosGrados, eliminarAlumnoGrado

urlpatterns = [
    url(r'^home$', listarAlumnosGrados.as_view(), name='listar'),
    url(r'^eliminarAlumnoGrado/(?P<pk>\d+)$', eliminarAlumnoGrado.as_view(), name='eliminar'),
    url(r'^editarAlumnoGrado/(?P<pk>\d+)$', editarAlumnoGrado.as_view(), name='editar'),
    url(r'^crearAlumnoGrado$', crearAlumnoGrado.as_view(), name = 'crear'),
]
