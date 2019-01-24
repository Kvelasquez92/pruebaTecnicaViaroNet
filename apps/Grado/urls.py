from django.conf.urls import url
from apps.Grado.views import crearGrado, editarGrado, listarGrados, eliminarGrado

urlpatterns = [
    url(r'^home$', listarGrados.as_view(), name='listar'),
    url(r'^eliminarGrado/(?P<pk>\d+)$', eliminarGrado.as_view(), name='eliminar'),
    url(r'^editarGrado/(?P<pk>\d+)$', editarGrado.as_view(), name='editar'),
    url(r'^crearGrado$', crearGrado.as_view(), name = 'crear'),
]
