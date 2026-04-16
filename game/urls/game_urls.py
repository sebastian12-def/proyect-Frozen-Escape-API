from django.urls import path
from game.views import *

urlpatterns = [
    path('usuarios/', crear_usuario),
    path('estado/<int:user_id>/', obtener_estado),
    path('accion/', ejecutar_accion),
    path('ranking/', ranking),
]