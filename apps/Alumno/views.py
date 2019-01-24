from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from apps.Alumno.models import Alumno
from apps.Alumno.forms import alumnoForm
from django.views.generic import CreateView, UpdateView, ListView, DeleteView

class crearAlumno(CreateView):
    form_class = alumnoForm
    template_name = 'alumno/crearAlumno.html'
    success_url = reverse_lazy('alumnos:listar')

class editarAlumno(UpdateView):
    model = Alumno
    form_class = alumnoForm
    template_name = 'alumno/editarAlumno.html'
    success_url = reverse_lazy('alumnos:listar')

class listarAlumnos(ListView):
    model = Alumno
    template_name = 'alumno/listarAlumnos.html'

class eliminarAlumno(DeleteView):
    model = Alumno
    template_name = 'alumno/eliminarAlumno.html'
    success_url = reverse_lazy('alumnos:listar')

    """def delete(self, request, *args, **kwargs):
       self.object = self.get_object()
       if self.object.nombre == request.nombre:
          self.object.delete()
          return HttpResponseRedirect(self.get_success_url())
       else:
          raise Http404("Ups! parece que este alumno no existe!")

    """
