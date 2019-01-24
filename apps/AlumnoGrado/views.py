from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from apps.Grado.models import Grado
from apps.Alumno.models import Alumno
from apps.AlumnoGrado.models import AlumnoGrado
from apps.AlumnoGrado.forms import alumnoGradoForm
from django.views.generic import CreateView, UpdateView, ListView, DeleteView

class crearAlumnoGrado(CreateView):
    form_class = alumnoGradoForm
    template_name = 'alumnogrado/crearAlumnoGrado.html'
    success_url = reverse_lazy('alumnosGrados:listar')

    def get_context_data(self, **kwargs):
        context = super(crearAlumnoGrado, self).get_context_data(**kwargs)
        context['alumnos'] = Alumno.objects.all()
        context['grados'] = Grado.objects.all()
        return context

class editarAlumnoGrado(UpdateView):
    model = AlumnoGrado
    form_class = alumnoGradoForm
    template_name = 'alumnogrado/editarAlumnoGrado.html'
    success_url = reverse_lazy('alumnosGrados:listar')

    def get_context_data(self, **kwargs):
        context = super(editarAlumnoGrado, self).get_context_data(**kwargs)
        context['alumno'] = self.object.alumnoId
        context['grado'] = self.object.gradoId
        context['alumnos'] = Alumno.objects.exclude(id=self.object.alumnoId.id)
        context['grados'] = Grado.objects.exclude(id=self.object.gradoId.id)
        return context

class listarAlumnosGrados(ListView):
    model = AlumnoGrado
    template_name = 'alumnogrado/listarAlumnoGrado.html'

class eliminarAlumnoGrado(DeleteView):
    model = AlumnoGrado
    template_name = 'alumnogrado/eliminarAlumnoGrado.html'
    success_url = reverse_lazy('alumnosGrados:listar')
