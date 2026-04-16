import random
from game.models import EstadoJugador, Accion

def ejecutar_accion_juego(user, accion_id):
    estado = EstadoJugador.objects.get(usuario=user)
    accion = Accion.objects.get(id=accion_id)

    # aplicar impacto base
    estado.temperatura += accion.impacto_temperatura
    estado.energia += accion.impacto_energia

    # evento aleatorio (bonus)
    evento = random.randint(-5, 5)
    estado.temperatura += evento

    # aumentar tiempo de supervivencia
    estado.tiempo_supervivencia += 1

    # validar muerte
    if estado.temperatura <= 0 or estado.energia <= 0:
        estado.save()
        return {
            "mensaje": "Has muerto",
            "estado": False
        }

    estado.save()

    return {
        "mensaje": "Acción ejecutada",
        "estado": True,
        "temperatura": estado.temperatura,
        "energia": estado.energia
    }