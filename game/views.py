from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth.models import User

from game.models import EstadoJugador
from game.serializers.user_serializer import UserSerializer
from game.serializers.estado_serializer import EstadoJugadorSerializer
from game.services.game_logic import ejecutar_accion_juego


# 🔹 Crear usuario
@api_view(['POST'])
def crear_usuario(request):
    serializer = UserSerializer(data=request.data)

    if serializer.is_valid():
        user = serializer.save()
        EstadoJugador.objects.create(usuario=user)
        return Response({"mensaje": "Usuario creado correctamente"})
    
    return Response(serializer.errors)


# 🔹 Consultar estado
@api_view(['GET'])
def obtener_estado(request, user_id):
    estado = EstadoJugador.objects.get(usuario_id=user_id)
    serializer = EstadoJugadorSerializer(estado)
    return Response(serializer.data)


# 🔹 Ejecutar acción
@api_view(['POST'])
def ejecutar_accion(request):
    user_id = request.data.get('user_id')
    accion_id = request.data.get('accion_id')

    user = User.objects.get(id=user_id)

    resultado = ejecutar_accion_juego(user, accion_id)

    return Response(resultado)


# 🔹 Ranking
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