from django.urls import path
from . import views

urlpatterns = [
    path('', views.EventoListView.as_view(), name='listar_eventos'),
    path('crear/', views.EventoCreateView.as_view(), name='crear_evento'),
    path('editar/<int:pk>/', views.EventoUpdateView.as_view(), name='editar_evento'),
    path('eliminar/<int:pk>/', views.EventoDeleteView.as_view(), name='eliminar_evento'),
]