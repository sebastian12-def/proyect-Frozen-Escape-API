from rest_framework import serializers
from game.models import Accion

class AccionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Accion
        fields = '__all__'