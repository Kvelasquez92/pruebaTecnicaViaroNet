from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from apps.Profesor.models import Profesor
from apps.Profesor.forms import profesorForm
from django.views.generic import CreateView, UpdateView, ListView, DeleteView

class crearProfesor(CreateView):
    form_class = profesorForm
    template_name = 'profesor/crearProfesor.html'
    success_url = reverse_lazy('profesores:listar')

class editarProfesor(UpdateView):
    model = Profesor
    form_class = profesorForm
    template_name = 'profesor/editarProfesor.html'
    success_url = reverse_lazy('profesores:listar')

class listarProfesores(ListView):
    model = Profesor
    template_name = 'profesor/listarProfesores.html'

class eliminarProfesor(DeleteView):
    model = Profesor
    template_name = 'profesor/eliminarProfesor.html'
    success_url = reverse_lazy('profesores:listar')
