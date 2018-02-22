from polla.views import templatepolla,obtenerPartidos,updatePartido,templatepollaApostar,saveApuesta,templatejuegopartidos
from django.urls import path

urlpatterns = [
#   path('trivia/', templated, name='templated'),
    path('mostrarpartidos/',templatepolla,name='mostrarpartidos'),
    path('obtenerPartidos/',obtenerPartidos,name='obtenerPartidos'),
    path('updatePartido/',updatePartido,name='updatePartido'),
    path('mostrarpartidosApostar/',templatepollaApostar,name='mostrarpartidosApostar'),
    path('saveApuesta/',saveApuesta,name='saveApuesta'),
    path('mostratjuegopolla/',templatejuegopartidos,name='mostratjuegopolla'),
    ]
