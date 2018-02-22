from trivia.views import  obtenerSalasadmin,score,iniciarjuegopracticatrivia,mostrarpregunta,guardarscore,obtenerSalas,pagar_sala,iniciarjuego,crearjuego,templated,templatetrivia
from django.urls import path

urlpatterns = [
    path('trivia/', templated, name='templated'),
    path('score/', score, name='Score'),
    path('mostrarpregunta/',mostrarpregunta,name='mostrarpregunta'),
    path('creartrivia/',templatetrivia,name='creartrivia'),
    path('crearjuego/',crearjuego,name='crearjuego'),
    path('iniciarjuego/',iniciarjuego,name='iniciarjuego'),
    path('obtenerSalas/',obtenerSalas,name='obtenerSalas'),
    path('pagar_sala/',pagar_sala,name='pagar_sala'),
    path('guardarscore/',guardarscore,name='guardarscore'),
    path('iniciarjuegopracticatrivia/',iniciarjuegopracticatrivia,name='iniciarjuegopracticatrivia'),
    path('obtenerSalasadmin/',obtenerSalasadmin,name='obtenerSalasadmintrivia')

    ]
