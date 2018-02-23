
from django.urls import path
from equipoideal import views

urlpatterns = [
    path('pagar_sala_EI/', views.pagar_sala, name='pagar_sala_EI'),
#    path('juegoequipoideal/', views.JuegoEquipoIdeal, name='juegoequipoideal'),
    path('jugadores/', views.retornarjugadores, name='retornarjugadores'),
    path('iniciarjuegoEI/',views.iniciarjuegoEI,name='iniciarjuegoEI'),
    path('obtenerSalasEI/',views.obtenerSalasEI,name='obtenerSalasEI'),
    path('obtenerSalasEIadmin/',views.obtenerSalasEIadmin,name='obtenerSalasEI'),
    path('crearequipoideal/',views.config_EI,name='config_EI'),
    path('crearjuegoEI/',views.crearjuegosala,name='crearjuegoEI'),
    path('iniciarjuegopracticaEIdeal/',views.iniciarjuegopracticaEIdeal,name='iniciarjuegopracticaEIdeal'),
    path('obtenerganadorEI/',views.Admin_calcularganadorEI,name='Admin_calcularganadorEI'),
    path('scoreEI/',views.guardarscore,name='scoreEI')
#"""
    ]
