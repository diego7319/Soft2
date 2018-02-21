
from django.urls import path
from equipoideal import views

urlpatterns = [
#    path('jugar/', vw, name='templated'),
    path('equipoideal/configurar', views.configurarjuego, name='configurarjuego'),
    path('juegoequipoideal/', views.JuegoEquipoIdeal, name='juegoequipoideal'),
    path('jugadores/', views.retornarjugadores, name='retornarjugadores'),

    ]
