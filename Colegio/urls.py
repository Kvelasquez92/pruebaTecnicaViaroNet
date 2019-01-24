"""Colegio URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import url, include

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^alumno/', include(('apps.Alumno.urls', 'Alumno'), namespace='alumnos')),
    url(r'^profesor/', include(('apps.Profesor.urls', 'Profesor'), namespace='profesores')),
    url(r'^grado/', include(('apps.Grado.urls', 'Grado'), namespace='grados')),
    url(r'^alumnoGrado/', include(('apps.AlumnoGrado.urls', 'AlumnoGrado'), namespace='alumnosGrados')),
]
