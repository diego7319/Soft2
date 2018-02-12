from trivia.views import  score,mostrarpregunta,obtenerSalas,iniciarjuego,crearjuego,templated,templatetrivia
from django.urls import path

urlpatterns = [
    path('trivia/', templated, name='templated'),
path('score/', score, name='Score'),
    path('mostrarpregunta/',mostrarpregunta,name='mostrarpregunta'),
    path('creartrivia/',templatetrivia,name='creartrivia'),
    path('crearjuego/',crearjuego,name='crearjuego'),
    path('iniciarjuego/',iniciarjuego,name='iniciarjuego'),
    path('getSalas/',obtenerSalas,name='obtenerSalas')

    ]
