from django.contrib.auth.models import User
from django.db import models

class Accion(models.Model):
    nombre = models.CharField(max_length=100)
    impacto_temperatura = models.IntegerField()
    impacto_energia = models.IntegerField()

    def __str__(self):
        return self.nombre


class EstadoJugador(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    temperatura = models.IntegerField(default=100)
    energia = models.IntegerField(default=100)
    recursos = models.IntegerField(default=50)
    tiempo_supervivencia = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.usuario.username} - Estado"