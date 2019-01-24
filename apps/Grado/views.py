from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from apps.Grado.models import Grado
from apps.Profesor.models import Profesor
from apps.Grado.forms import gradoForm
from django.views.generic import CreateView, UpdateView, ListView, DeleteView

class crearGrado(CreateView):
    form_class = gradoForm
    template_name = 'grado/crearGrado.html'
    success_url = reverse_lazy('grados:listar')

    def get_context_data(self, **kwargs):
        context = super(crearGrado, self).get_context_data(**kwargs)
        context['profesores'] = Profesor.objects.all()
        return context

class editarGrado(UpdateView):
    model = Grado
    form_class = gradoForm
    template_name = 'grado/editarGrado.html'
    success_url = reverse_lazy('grados:listar')

    def get_context_data(self, **kwargs):
        context = super(editarGrado, self).get_context_data(**kwargs)
        context['profesor'] = self.object.profesorId
        context['profesores'] = Profesor.objects.exclude(id=self.object.profesorId.id)
        return context

class listarGrados(ListView):
    model = Grado
    template_name = 'grado/listarGrados.html'

class eliminarGrado(DeleteView):
    model = Grado
    template_name = 'grado/eliminarGrado.html'
    success_url = reverse_lazy('grados:listar')
