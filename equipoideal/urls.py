
from django.urls import path
from equipoideal import views

urlpatterns = [
#    path('jugar/', vw, name='templated'),
    path('juegoequipoideal/', views.JuegoEquipoIdeal, name='juegoequipoideal'),
    path('jugadores/', views.retornarjugadores, name='retornarjugadores'),
    path('crearequipoideal/',views.templateequipoideal,name='templateequipoideal'),
    path('obtenerSalasEI/',views.obtenerSalasEI,name='obtenerSalasEI')

    ]
