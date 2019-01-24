from django.conf.urls import url
from apps.Profesor.views import crearProfesor, editarProfesor, listarProfesores, eliminarProfesor

urlpatterns = [
    url(r'^home$', listarProfesores.as_view(), name='listar'),
    url(r'^eliminarProfesor/(?P<pk>\d+)$', eliminarProfesor.as_view(), name='eliminar'),
    url(r'^editarProfesor/(?P<pk>\d+)$', editarProfesor.as_view(), name='editar'),
    url(r'^crearProfesor$', crearProfesor.as_view(), name = 'crear'),
]
