from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
# Importamos PermissionRequiredMixin
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse_lazy
from .models import Evento
from django.shortcuts import render, redirect # <--- Agrega redirect
from django.contrib import messages # <--- Agrega messages
# Listar: Solo requiere login (Todos pueden ver)

# Este mixin intercepta el error 403 y lo convierte en un mensaje amigable
class PermisoMensajeMixin:
    def handle_no_permission(self):
        messages.error(self.request, "No tienes permisos para realizar esta operación.")
        return redirect('listar_eventos')
class EventoListView(LoginRequiredMixin, ListView):
    model = Evento
    template_name = 'eventos/lista_eventos.html'
    context_object_name = 'eventos'

# Crear: Requiere login Y permiso de agregar ('add_evento')
class EventoCreateView(PermisoMensajeMixin, LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Evento
    template_name = 'eventos/evento_form.html'
    fields = ['titulo', 'descripcion', 'fecha', 'lugar']
    success_url = reverse_lazy('listar_eventos')
    permission_required = 'eventos.add_evento' # <--- Permiso necesario

    def form_valid(self, form):
        form.instance.organizador = self.request.user
        return super().form_valid(form)

# Editar: Requiere login Y permiso de cambiar ('change_evento')
class EventoUpdateView(PermisoMensajeMixin, LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Evento
    template_name = 'eventos/evento_form.html'
    fields = ['titulo', 'descripcion', 'fecha', 'lugar']
    success_url = reverse_lazy('listar_eventos')
    permission_required = 'eventos.change_evento' # <--- Permiso necesario

# Eliminar: Requiere login Y permiso de borrar ('delete_evento')
class EventoDeleteView(PermisoMensajeMixin, LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Evento
    template_name = 'eventos/evento_confirm_delete.html'
    success_url = reverse_lazy('listar_eventos')
    permission_required = 'eventos.delete_evento' # <--- Solo Admin lo tiene