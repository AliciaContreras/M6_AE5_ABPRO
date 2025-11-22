from django.db import models
from django.contrib.auth.models import User

class Evento(models.Model):
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField()
    fecha = models.DateTimeField()
    lugar = models.CharField(max_length=100)
    # El organizador es el usuario que crea el evento
    organizador = models.ForeignKey(User, on_delete=models.CASCADE, related_name='eventos_creados')
    
    def __str__(self):
        return f"{self.titulo} ({self.fecha.strftime('%d/%m/%Y')})"