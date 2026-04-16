import random

from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from game.models import Accion, EstadoJugador
from game.serializers.user_serializer import UserSerializer
from game.serializers.estado_serializer import EstadoJugadorSerializer


#  Crear usuario
@api_view(['POST'])
def crear_usuario(request):
    serializer = UserSerializer(data=request.data)

    if serializer.is_valid():
        user = serializer.save()
        EstadoJugador.objects.create(usuario=user)
        return Response({"mensaje": "Usuario creado correctamente"})
    
    return Response(serializer.errors)


#  Consultar estado
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def obtener_estado(request):
    estado = EstadoJugador.objects.get(usuario=request.user)
    serializer = EstadoJugadorSerializer(estado)
    return Response(serializer.data)


#  Ejecutar acción
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def ejecutar_accion(request):
    user = request.user
    accion_id = request.data.get('accion_id')
    accion = get_object_or_404(Accion, id=accion_id)
    estado = EstadoJugador.objects.get(usuario=user)

    random_temp = random.randint(-5, 5)
    random_energy = random.randint(-5, 5)

    estado.temperatura += accion.impacto_temperatura + random_temp
    estado.energia += accion.impacto_energia + random_energy

    estado.temperatura = max(0, min(100, estado.temperatura))
    estado.energia = max(0, min(100, estado.energia))

    estado.save()

    if estado.temperatura <= 0 or estado.energia <= 0:
        return Response({
            "mensaje": "Has perdido",
            "estado": "game over"
        })

    return Response({
        "mensaje": "Acción ejecutada",
        "temperatura": estado.temperatura,
        "energia": estado.energia
    })


#  Ranking
@api_view(['GET'])
def ranking(request):
    estados = EstadoJugador.objects.all().order_by('-tiempo_supervivencia')[:10]

    data = [
        {
            "usuario": e.usuario.username,
            "tiempo": e.tiempo_supervivencia
        }
        for e in estados
    ]

    return Response(data)