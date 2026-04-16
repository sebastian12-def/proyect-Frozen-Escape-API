from rest_framework import serializers
from game.models import EstadoJugador


class EstadoJugadorSerializer(serializers.ModelSerializer):
    usuario = serializers.CharField(source='usuario.username', read_only=True)

    class Meta:
        model = EstadoJugador
        fields = ('usuario', 'temperatura', 'energia', 'recursos', 'tiempo_supervivencia')
